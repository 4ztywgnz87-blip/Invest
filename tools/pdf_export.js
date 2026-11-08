// HTML-rapport -> PDF (A4), met alle inklapbare secties opengeklapt.
// Slimme pagina-indeling: een hoofdstuk dat in het onderste deel van een pagina zou
// beginnen (en daar niet volledig past), start op een nieuwe pagina.
// Gebruik: node tools/pdf_export.js rapport.html rapport.pdf
const { chromium } = require('playwright');
const path = require('path');

const MM = 96 / 25.4;                       // px per mm
const MARGE = { top: 14, bottom: 16, left: 12, right: 12 };
const BREEDTE = (210 - MARGE.left - MARGE.right) * MM;
const HOOGTE = (297 - MARGE.top - MARGE.bottom) * MM;
const ONDERSTE_DEEL = 0.33;                 // start niet in het onderste derde van een pagina

(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: Math.round(BREEDTE), height: 1000 } });
  await page.goto('file://' + path.resolve(inp));
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(({ HOOGTE, ONDERSTE_DEEL }) => {
    document.querySelectorAll('details').forEach(d => { if (!d.classList.contains('g-tabel')) d.open = true; });
    // We werken in de doorlopende (schermweergave van de print-)layout en duwen elementen naar de
    // volgende pagina met een onzichtbare opvulling. Zo blijft de berekening na elke ingreep exact.
    const HOOFD = '.pdf-blok';
    const SAMEN = '.grafiek-blok, .kader, .kerncijfers, .scenarios, .vlag, .tabelwrap';
    const els = [...document.querySelectorAll(HOOFD + ',' + SAMEN)];
    const basis = document.body.getBoundingClientRect().top + window.scrollY;   // begin van pagina 1
    for (const el of els) {
      const r = el.getBoundingClientRect();
      const top = r.top + window.scrollY - basis;
      const opPagina = top % HOOGTE;
      const rest = HOOGTE - opPagina;
      if (opPagina < 8 || r.height <= rest) continue;           // past, of staat al bovenaan
      let duw = false;
      if (el.matches(HOOFD)) {
        const min = el.classList.contains('pdf-klein') ? 140 : HOOGTE * ONDERSTE_DEEL;
        duw = rest < min;
      } else {
        duw = r.height < HOOGTE * 0.9;                          // klein genoeg om heel te houden
      }
      if (duw) {
        const vul = document.createElement('div');
        vul.style.height = rest + 'px';
        el.parentNode.insertBefore(vul, el);
      }
    }
  }, { HOOGTE, ONDERSTE_DEEL });
  await page.pdf({
    path: out, format: 'A4', printBackground: true,
    margin: { top: MARGE.top + 'mm', bottom: MARGE.bottom + 'mm', left: MARGE.left + 'mm', right: MARGE.right + 'mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;color:#777;width:100%;text-align:center;">Pagina <span class="pageNumber"></span> / <span class="totalPages"></span> — onderzoek en mening, geen gereglementeerd financieel advies</div>',
  });
  await browser.close();
})();
