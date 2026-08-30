"""Emite as fotos de fotos/ como data URIs, para o deck nao depender de arquivos externos."""
import base64, json, mimetypes, pathlib, sys

pasta = pathlib.Path(sys.argv[1])
mapa = {}
if pasta.is_dir():
    for f in sorted(pasta.iterdir()):
        if f.suffix.lower() not in ('.jpg', '.jpeg', '.png', '.webp'):
            continue
        tipo = mimetypes.guess_type(f.name)[0] or 'image/jpeg'
        b64 = base64.b64encode(f.read_bytes()).decode()
        # A chave e o nome-base, igual ao data-img declarado no slot.
        mapa[f'{pasta.name}/{f.stem}'] = f'data:{tipo};base64,{b64}'
if mapa:
    print('<script>window.__FOTOS=' + json.dumps(mapa, separators=(',', ':')) + ';</script>')
    print(f'<!-- {len(mapa)} foto(s) embutida(s) -->', file=sys.stderr)
