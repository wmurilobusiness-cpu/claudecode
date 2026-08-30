# Fotos

Coloque aqui os arquivos de imagem do deck, um por slot.

Nomeie pelo slot para que a manutenção seja óbvia:
`slot-01.jpg`, `slot-02a.jpg`, `slot-02b.jpg`, `slot-02c.jpg`, `slot-03.jpg` … `slot-13.jpg`.

Para ligar uma foto ao slide, edite `deck/_body.html` e acrescente `--img` ao slot correspondente:

```html
<div class="ph bleed r g-left" data-slot="01"
     style="width:44%;--img:url('fotos/slot-01.jpg');--pos:center 30%">
```

`--pos` controla o enquadramento dentro do slot (padrão `center`). Use `center 30%` para subir o
recorte quando o rosto ficar baixo demais, `center 70%` para descer.

Depois rode `./deck/build.sh` e `python3 deck/export.py`.

O briefing de casting e as marcas de enquadramento somem automaticamente quando `--img` é definido —
não é preciso apagar nada. O tratamento visual (contraste, dessaturação, pretos, grão e gradiente de
leitura) é aplicado pelo CSS, igual em todos os slots.

Especificação completa de cada slot: `../DIRECAO-DE-IMAGEM.md`.
