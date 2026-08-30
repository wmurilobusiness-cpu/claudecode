# Fotos

Coloque aqui os 8 arquivos, com estes nomes-base:

| Nome do arquivo | Qual foto |
| --- | --- |
| `slot-01` | Academia, parede preta, você encostado, bandana |
| `slot-02a` | Palco, pose de abdominal e coxa, nº 524 |
| `slot-02b` | Palco, troféu erguido |
| `slot-02c` | Vestiário, parede preta com faixa vermelha |
| `slot-03` | Azulejo bege, pose lateral |
| `slot-05` | Azulejo bege, front lat spread |
| `slot-10` | Azulejo bege, front double biceps |
| `slot-13` | Azulejo bege, rear lat spread de braços abertos |

**A extensão não importa.** O deck procura sozinho por `.jpg`, `.jpeg`, `.png` e `.webp`,
maiúsculas incluídas — não é preciso renomear nem converter. A única exceção é **HEIC**
(padrão do iPhone), que navegador nenhum abre: se o arquivo for `.heic`, converta para JPEG antes.

Pronto. Nenhuma outra edição é necessária — o briefing de casting some sozinho e o tratamento
visual é aplicado automaticamente.

Se um recorte cortar mal, ajuste o `--pos` do slot em `deck/_body.html`: `center 30%` sobe o
enquadramento, `center 70%` desce.

Depois rode `./deck/build.sh` e `python3 deck/export.py` para regerar o PDF e os PNGs.

Especificação completa de cada slot: `../DIRECAO-DE-IMAGEM.md`.
