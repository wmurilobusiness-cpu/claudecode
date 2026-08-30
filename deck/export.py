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
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=2)
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
        pg.screenshot(path=str(PNG / f'{name}.png'), scale='css')  # 1920x1080 exatos
    print(f'{len(slides)} PNGs -> {PNG}')

    # O PDF e montado a partir de capturas em 2x e recomprimidas em JPEG.
    # O caminho pelo print CSS produzia um PDF de 27 MB, porque o Chromium grava
    # as fotos sem perdas; aqui o mesmo deck cabe em poucos megabytes.
    paginas = []
    pg.set_viewport_size({'width': 1920, 'height': 1080})
    for i in range(len(slides)):
        pg.evaluate("i => document.querySelectorAll('.slide').forEach((s,j)=>s.classList.toggle('is-live', j===i))", i)
        pg.wait_for_timeout(1400)
        paginas.append(pg.screenshot(type='jpeg', quality=82, scale='css'))
    b.close()

import io
from PIL import Image
quadros = [Image.open(io.BytesIO(b)).convert('RGB') for b in paginas]
quadros[0].save(PDF, save_all=True, append_images=quadros[1:],
                resolution=96.0, quality=82, optimize=True)
print(f'PDF -> {PDF} ({PDF.stat().st_size // 1024} KB)')
