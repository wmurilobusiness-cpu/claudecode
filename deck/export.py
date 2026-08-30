"""Exports the deck to a 1920x1080 PDF and one PNG per slide."""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PNG  = ROOT / 'export' / 'png'
PNG.mkdir(parents=True, exist_ok=True)
for stale in PNG.glob('*.png'):  # slide titles change between versions
    stale.unlink()
PDF  = ROOT / 'export' / 'Metodo-1porcento-Apresentacao-de-Vendas.pdf'

with sync_playwright() as p:
    b  = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
    pg.goto((ROOT / 'index.html').as_uri())
    pg.wait_for_timeout(2500)

    slides = pg.evaluate("""() => [...document.querySelectorAll('.slide')].map(
        (s,i) => String(i+1).padStart(2,'0') + '-' + s.dataset.title
            .toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')
            .replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''))""")

    pg.evaluate("document.getElementById('nav').hidden = true")
    for i, name in enumerate(slides):
        pg.evaluate("i => document.querySelectorAll('.slide').forEach((s,j)=>s.classList.toggle('is-live', j===i))", i)
        pg.wait_for_timeout(120)
        pg.screenshot(path=str(PNG / f'{name}.png'))
    print(f'{len(slides)} PNGs -> {PNG}')

    # print CSS lays every slide out at exact size, one per page
    pg.pdf(path=str(PDF), width='1920px', height='1080px',
           print_background=True, prefer_css_page_size=True, margin={'top':'0','right':'0','bottom':'0','left':'0'})
    print(f'PDF -> {PDF}')
    b.close()
