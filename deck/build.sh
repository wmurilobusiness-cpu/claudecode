#!/usr/bin/env bash
# Gera o index.html a partir de deck/_body.html.
# As fotos de fotos/ entram embutidas em base64, como as fontes: o arquivo resultante
# e autossuficiente — abre offline, vai por e-mail e publica como Artifact sem
# depender de nenhum caminho relativo.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
raiz="$(dirname "$here")"
src="$here/_body.html"
split=$(grep -n '^<div id="deck">' "$src" | head -1 | cut -d: -f1)
[ -n "$split" ] || { echo "raiz do deck nao encontrada" >&2; exit 1; }
{
  echo '<!doctype html>'
  echo '<html lang="pt-BR">'
  echo '<head>'
  echo '<meta charset="utf-8">'
  echo '<meta name="viewport" content="width=device-width, initial-scale=1">'
  sed -n "1,$((split-1))p" "$src"
  echo '<style>html,body{margin:0;padding:0;background:#06070A;color-scheme:dark}img{max-width:100%}</style>'
  echo '</head>'
  echo '<body>'
  # As fotos precisam existir ANTES do script do deck rodar, senao ele cai no
  # caminho de arquivo local — que nao existe no Artifact publicado.
  python3 "$here/embed_fotos.py" "$raiz/fotos"
  sed -n "${split},\$p" "$src"
  echo '</body>'
  echo '</html>'
} > "$raiz/index.html"
echo "index.html gerado ($(( $(wc -c < "$raiz/index.html") / 1024 )) KB)"

# Versao para publicar como Artifact: mesmo conteudo, sem o esqueleto HTML
# (o host fornece doctype/head/body) e com as fotos ja embutidas.
{
  sed -n "1,$((split-1))p" "$src"
  python3 "$here/embed_fotos.py" "$raiz/fotos" 2>/dev/null
  sed -n "${split},\$p" "$src"
} > "$here/_artifact.html"
echo "_artifact.html gerado ($(( $(wc -c < "$here/_artifact.html") / 1024 )) KB)"
