// HTML-rapport -> PDF (A4), met alle inklapbare secties opengeklapt.
// Gebruik: node tools/pdf_export.js rapport.html rapport.pdf
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(inp));
  await page.evaluate(() => {
    document.querySelectorAll('details').forEach(d => {
      if (!d.classList.contains('g-tabel')) d.open = true;
    });
  });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({
    path: out, format: 'A4', printBackground: true,
    margin: { top: '14mm', bottom: '16mm', left: '12mm', right: '12mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;color:#777;width:100%;text-align:center;">Pagina <span class="pageNumber"></span> / <span class="totalPages"></span> — onderzoek en mening, geen gereglementeerd financieel advies</div>',
  });
  await browser.close();
})();
