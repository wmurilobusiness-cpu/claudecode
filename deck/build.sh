#!/usr/bin/env bash
# Wraps deck/_body.html into a standalone HTML document for local viewing and PDF export.
# The same _body.html is published as an Artifact, where the host supplies the skeleton.
# Split point: everything before `<div id="deck">` is metadata (title + styles) -> <head>.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
src="$here/_body.html"
split=$(grep -n '^<div id="deck">' "$src" | head -1 | cut -d: -f1)
[ -n "$split" ] || { echo "deck root not found" >&2; exit 1; }
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
  sed -n "${split},\$p" "$src"
  echo '</body>'
  echo '</html>'
} > "$here/../index.html"
echo "built index.html ($(wc -c < "$here/../index.html") bytes)"
