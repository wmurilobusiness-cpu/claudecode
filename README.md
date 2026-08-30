# Método 1% — Apresentação de Vendas

Deck de vendas da consultoria **ONEPERCENT1% · Elite Training System** (Wilton Murilo).
13 slides, 16:9, 1920×1080.

## Arquivos

| Arquivo | O que é |
| --- | --- |
| `index.html` | O deck. Abra no navegador e apresente em tela cheia. |
| `ROTEIRO-DE-CALL.md` | Por slide: título, copy, layout, imagem, tipografia, animações, speaker notes, objetivo psicológico e transição. |
| `DIRECAO-DE-IMAGEM.md` | Curadoria dos 15 slots de foto: casting, recorte, resolução mínima, posição e tratamento. |
| `fotos/` | Onde entram os arquivos de imagem. Veja `fotos/LEIA-ME.md`. |
| `export/Metodo-1porcento-Apresentacao-de-Vendas.pdf` | PDF 1920×1080, 13 páginas. |
| `export/png/` | Um PNG 1920×1080 por slide. |
| `deck/_body.html` | Fonte do deck. **Edite aqui**, nunca no `index.html`. |
| `deck/fonts.css` | Bebas Neue e Barlow embutidas em base64 (subset latin, OFL). |
| `deck/build.sh` | Gera o `index.html` a partir do `_body.html`. |
| `deck/export.py` | Gera o PDF e os PNGs. |

## Estrutura comercial

`promessa → autoridade → problema → quebra de crença → mecanismo → entrega → valor percebido →
investimento principal → condição especial → redução de risco → decisão`

| Slide | Função |
| --- | --- |
| 1 | Hook |
| 2 | Autoridade |
| 3 | Problema real |
| 4 | Os 4 vazamentos |
| 5 | Quebra de crenças |
| 6 | Mecanismo — Método 1% |
| 7 | Ciclo 4A |
| 8 | Entrega |
| 9 | Valor percebido — âncora R$ 5.982 |
| 10 | Investimento principal — 12x R$ 300 / R$ 3.000 |
| 11 | Condição de entrada — 12x R$ 149,70 / R$ 1.497 |
| 12 | Redução de risco |
| 13 | Fechamento |

A pergunta de investimento acontece **com o slide 9 na tela**, antes de avançar para o 10. O roteiro
traz o script e as três ramificações de resposta.

## Apresentar

Abra `index.html` no navegador e use F11 (tela cheia).

| Tecla | Ação |
| --- | --- |
| `→` `espaço` `PageDown` | Próximo slide |
| `←` `PageUp` | Slide anterior |
| `Home` / `End` | Primeiro / último slide |
| `B` | Mostra/esconde os briefings de casting dos slots vazios |

Cada slide entra com uma animação escalonada de 520ms, desativada para quem usa
`prefers-reduced-motion` e no PDF. Slot de foto ainda vazio aparece como painel escuro, não como
briefing — o deck está sempre apresentável. A tecla `B` revela os briefings quando você for
escolher as imagens. O deck escala sozinho para qualquer tela; a barra de navegação
some no PDF.

## Editar

1. Altere `deck/_body.html`.
2. `./deck/build.sh` — regenera o `index.html`.
3. `python3 deck/export.py` — regenera PDF e PNGs.

### Três campos que precisam ser preenchidos antes de usar

**Slide 11 — escopo da condição de entrada.** A caixa tracejada `ESCOPO DESTA CONDIÇÃO` está em branco
de propósito. Preencha com o que diferencia essa condição do programa completo (ciclo mais curto, menos
reavaliações, escopo reduzido). Sem isso, as duas condições viram o mesmo pacote por preços
diferentes — veja "Regras comerciais" no roteiro.

**Slide 12 — política de arrependimento.** A caixa `ARREPENDIMENTO: 7 DIAS` só deve permanecer se a
política existir no seu contrato. Se não existir, apague a `div.editable.final`.

**Slide 2 — certificação ACSM.** O chip traz "Personal Trainer certificado · ACSM · EUA". Confirme a
nomenclatura oficial da credencial e ajuste antes de publicar.

### Inserir as fotos

São 15 slots de imagem nos 13 slides. Cada um é um `<div class="ph">` com um briefing de casting
visível enquanto está vazio. Para preencher, acrescente `--img` ao slot:

```html
<div class="ph bleed r g-left" data-slot="01"
     style="width:44%;--img:url('fotos/slot-01.jpg');--pos:center 30%">
```

`--pos` ajusta o enquadramento dentro do slot (`center 30%` sobe o recorte, `center 70%` desce).
O briefing e as marcas de enquadramento somem sozinhos — não é preciso apagar nada.

O tratamento visual é aplicado por CSS, igual em todos os slots: contraste `1.14`, saturação `0.84`,
brilho `0.88`, grão cinematográfico e gradiente de leitura por slot. É correção de cor, não retoque:
nada altera físico, rosto ou proporções.

Quatro slots são de fundo (slides 4, 7, 9 e 11) e ficam invisíveis quando vazios — o slide funciona
sem eles. Nos slides 9 e 11 a recomendação é justamente deixá-los vazios, para que os números
dominem.

Especificação completa de cada slot: `DIRECAO-DE-IMAGEM.md`.

## Identidade visual

| Token | Valor | Uso |
| --- | --- | --- |
| `--ink` | `#06070A` | Fundo |
| `--graphite` / `--graphite-2` | `#101216` / `#171A1F` | Cards |
| `--steel` / `--steel-2` | `#262B32` / `#343A43` | Filetes e bordas |
| `--red` / `--red-hot` | `#D8071F` / `#FF2436` | Acento ONEPERCENT |
| `--silver` / `--silver-dim` | `#C3C9D1` / `#7C848E` | Metálico, apoio |
| `--paper` / `--muted` | `#F2F4F6` / `#8B929B` | Texto |

**Bebas Neue** é a fonte dominante: headlines, títulos, números, etiquetas, destaques e CTAs.
**Barlow** aparece apenas em texto corrido, onde a caixa alta condensada prejudicaria a leitura.
As duas estão embutidas em base64 — o deck renderiza idêntico offline, no PDF e em qualquer máquina.

Cada slide tem uma moldura de instrumento: trilha de 13 setores no topo que preenche conforme a
apresentação avança, wordmark à esquerda e leitura `FASE | 10 / 13` à direita.

## Regras de conteúdo

O deck não contém promessa de resultado, prazo de transformação, falsa urgência, escassez inventada,
número não fornecido ou claim médico. O slide 12 declara explicitamente o que não é garantido. Os
únicos valores são a escada de preços fixa (R$ 5.982 · 12x R$ 300 / R$ 3.000 · 12x R$ 149,70 /
R$ 1.497). Mantenha isso ao editar.
