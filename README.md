# Método 1% — Apresentação de Vendas

Deck de vendas da consultoria **ONEPERCENT1% · Elite Training System** (Wilton Murilo).
13 slides, 16:9, 1920×1080.

## Arquivos

| Arquivo | O que é |
| --- | --- |
| `index.html` | O deck. Abra no navegador e apresente em tela cheia. |
| `ROTEIRO-DE-CALL.md` | Título, texto, layout, foto sugerida e speaker notes de cada slide. |
| `export/Metodo-1porcento-Apresentacao-de-Vendas.pdf` | PDF 1920×1080, 13 páginas. |
| `export/png/` | Um PNG 1920×1080 por slide (para Instagram, Canva ou PowerPoint). |
| `deck/_body.html` | Fonte do deck. **Edite aqui**, nunca no `index.html`. |
| `deck/build.sh` | Gera o `index.html` a partir do `_body.html`. |
| `deck/export.py` | Gera o PDF e os PNGs. |

## Apresentar

Abra `index.html` no navegador e use F11 (tela cheia).

| Tecla | Ação |
| --- | --- |
| `→` `espaço` `PageDown` | Próximo slide |
| `←` `PageUp` | Slide anterior |
| `Home` / `End` | Primeiro / último slide |

O deck escala sozinho para qualquer tela. A barra inferior (setas e pontos) some no PDF.

## Editar

1. Altere `deck/_body.html`.
2. `./deck/build.sh` — regenera o `index.html`.
3. `python3 deck/export.py` — regenera PDF e PNGs.

### Preencher os valores da oferta (slide 11)

Os campos de preço são os `<span class="blank">` dentro do bloco `.price`. Substitua o span
pelo valor:

```html
<div class="main">12x <u>R$ 497</u></div>
<div class="alt">R$ 4.970 à vista</div>
```

Se o bônus não se aplicar, apague a `<div class="bonus">` inteira.

### Inserir as fotos

O slide 1 tem um painel de imagem à direita (`.hero-bleed`). Para usar uma foto real, adicione
a imagem ao `background` do painel e remova a legenda `.cap`:

```html
<div class="hero-bleed" style="background-image:url('foto.jpg');background-size:cover;
     background-position:center">
```

O `::after` do painel já aplica o degradê que funde a foto com o fundo preto.

## Identidade visual

| Token | Valor | Uso |
| --- | --- | --- |
| `--ink` | `#06070A` | Fundo |
| `--graphite` / `--graphite-2` | `#101216` / `#171A1F` | Cards |
| `--steel` | `#262B32` | Filetes e bordas |
| `--red` / `--red-hot` | `#D8071F` / `#FF2436` | Acento ONEPERCENT |
| `--silver` | `#C3C9D1` | Metálico, textos de apoio |
| `--paper` / `--muted` | `#F2F4F6` / `#8B929B` | Texto |

Tipografia: **Archivo** (títulos), **Barlow** (texto), **IBM Plex Mono** (dados e etiquetas).
As três estão embutidas no arquivo em base64 — o deck renderiza idêntico offline, no PDF e em
qualquer máquina, sem depender de internet.

## Regras de conteúdo

O deck foi escrito para não conter: promessa de resultado, prazo de transformação, número
não fornecido, formação não informada ou claim médico. Os gráficos dos slides 3 e 6 são
marcados como **representação conceitual** — são diagramas de ideia, não dados. O slide 12
declara explicitamente o que não é garantido. Mantenha isso ao editar.
