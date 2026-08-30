# Direção de Imagem — Método 1%
**ONEPERCENT1% · Elite Training System — Wilton Murilo**

Especificação dos 15 slots de imagem dos 13 slides: o que cada foto precisa ser, como entra na
composição e como é tratada.

## Curadoria aplicada

As fotos chegaram dentro do PDF exportado do Canva e foram extraídas de lá. São **cinco** — o Canva
não recebeu as demais. Estão embutidas no deck em base64, como as fontes: `index.html` é
autossuficiente, abre offline e vai por e-mail sem pasta de apoio.

| Slot | Foto | Por que ali |
| --- | --- | --- |
| **01** Hook | Vestiário, parede preta com faixa vermelha | Única com a paleta exata do deck e espaço negativo à esquerda para a headline. A faixa vermelha da bancada casa com a marca |
| **02A** Autoridade | Palco, troféu erguido | Resultado, não esforço. Vertical, sujeito grande no quadro |
| **02B** Bastidor | Dia de competição | Miniatura larga sob o retrato principal, legendada — humaniza sem virar álbum |
| **03** Problema real | Academia escura, neon vermelho, figura sozinha de cabeça baixa | O melhor achado do conjunto. Paleta exata e a imagem literal da estagnação. Figura anônima funciona melhor que um retrato: o prospect se projeta nela |
| **13** Fechamento | Palco, pose de abdominal e coxa, corpo inteiro | Postura dominante, fecha o arco aberto no slide 1 sem repetir a foto |

Slots **05** e **10** ficaram sem foto e aparecem como painel escuro. Slides **08** e **12** estão em
largura cheia, sem coluna de imagem.

### O que a volta pelo Canva quebrou

| Problema | Causa | Correção |
| --- | --- | --- |
| "Estratégia, Performance e Transformação" virou uma **barra branca sólida** | `background-clip:text` não sobrevive à exportação entre ferramentas | Trocado por prata sólido — o construto frágil saiu do deck |
| Cards de estatística embaralhados, rótulos sobrepostos | Reflow na importação | Regenerado do fonte, que nunca teve o problema |
| Foto errada em cada slide | As imagens foram posicionadas sem seguir a curadoria | Recolocadas por função |

A correção não foi feita em cima do PDF do Canva: as fotos foram extraídas dele e o deck foi
regerado do fonte, que é fiel por construção.

### Lacunas que continuam

| Prioridade | Slot | O que falta |
| --- | --- | --- |
| 1 | **12** | Retrato olhando para a câmera, sem pose — é o slide em que você diz o que não garante |
| 2 | **08** | Você trabalhando: celular, computador, orientando alguém |
| 3 | **06** | Carro ou detalhe de engenharia (slide limpo enquanto não existe) |
| 4 | **05** | Treino pesado com carga real |
| 5 | **10** | Retrato sóbrio, enquadramento fechado |

Futebol e Estados Unidos seguem sem imagem — são as duas que mais individualizariam o deck.

--- | --- | --- | --- |
| P01 | Palco NPC, pose de abdominal e coxa, banner Muscle Contest, nº 524 | Bodybuilding | **slot 02A** |
| P02 | Palco, troféu erguido, sorrindo, nº 524 | Storytelling | **slot 02B** |
| P03 | Academia, parede preta texturizada, bandana, encostado, shorts cinza | Hero / Autoridade | **slot 01** |
| P04 | Banheiro cinza, selfie de espelho, camiseta erguida, celular laranja | Descartar | — |
| P05 | McDonald's, camiseta erguida, bandeja de Big Macs | Descartar | — |
| P06 | Azulejo bege, front double biceps, corpo inteiro | Bodybuilding | **slot 10** |
| P07 | Azulejo bege, pose lateral / side chest | Performance | **slot 03** |
| P08 | Azulejo bege, costas com mãos na cintura | Descartar (repetição) | — |
| P09 | Azulejo bege, rear double biceps | Descartar (repetição) | — |
| P10 | Azulejo bege, front lat spread, tensão máxima | Performance | **slot 05** |
| P11 | Azulejo bege, rear lat spread com braços abertos | Bodybuilding | **slot 13** |
| P12 | Vestiário, parede preta com faixa vermelha, torso, celular laranja | Profissional | **slot 02C** |

### Arquivos a salvar

A extensão não importa — o deck procura por `.jpg`, `.jpeg`, `.png` e `.webp` sozinho. Só HEIC
não funciona em navegador: converta para JPEG antes.

| Salvar como | Qual foto |
| --- | --- |
| `fotos/slot-01` | P03 — academia, parede preta, encostado |
| `fotos/slot-02a` | P01 — palco, pose de abdominal e coxa |
| `fotos/slot-02b` | P02 — palco, troféu erguido |
| `fotos/slot-02c` | P12 — vestiário, parede preta e faixa vermelha |
| `fotos/slot-03` | P07 — azulejo, pose lateral |
| `fotos/slot-05` | P10 — azulejo, front lat spread |
| `fotos/slot-10` | P06 — azulejo, front double biceps |
| `fotos/slot-13` | P11 — azulejo, rear lat spread com braços abertos |

### Por que estes descartes

**P04 (banheiro) e P05 (McDonald's)** caem pelos seus próprios critérios: selfie casual demais, fundo
poluído (mictórios, saboneteira) e, no caso do McDonald's, uma paleta laranja e amarela que briga
frontalmente com preto, grafite e vermelho. P05 é boa foto de rede social; não é foto de consultoria
premium.

**P08 e P09** são boas, mas seriam a quinta e a sexta imagem da mesma sessão de azulejo. Já uso
quatro dela — que é o limite do aceitável antes de o deck parecer um ensaio só.

### Correção de temperatura

A sessão de azulejo bege (P06, P07, P10, P11) tem fundo quente, o oposto da paleta. Esses quatro
slots recebem uma correção adicional — saturação 0.50, brilho 0.72 e leve rotação de matiz para o
frio — que os traz para o preto e grafite sem tocar no físico nem no tom de pele. Sem isso, quatro
slides puxariam o deck inteiro para o bege.

### Lacunas do acervo

Cinco slots continuam sem foto adequada, e nenhuma imagem recebida os resolve. Estas são as fotos
que mais valem a pena buscar ou produzir, em ordem de impacto:

| Prioridade | Slot | O que falta | Por que importa |
| --- | --- | --- | --- |
| 1 | **12** | Retrato olhando direto para a câmera, expressão séria e aberta, **sem pose** | É o slide em que você diz o que não garante. Uma foto posada ali contradiz a honestidade do texto — por isso deixei vazio em vez de forçar |
| 2 | **08** | Você trabalhando: celular, computador, orientando alguém, conferindo execução | É o slide do acompanhamento. Todo o acervo mostra o físico; nenhuma foto mostra o trabalho, que é exatamente o que você vende |
| 3 | **06** | Porsche ou detalhe de engenharia | Sem ela o slide funciona (deixei o fundo silencioso), mas é a metáfora central do método |
| 4 | **02B** | Futebol — foto histórica | Os 13 anos são afirmados em texto e não provados em imagem |
| 5 | **02C** | Estados Unidos | Idem, para os 6 anos |

Os slots 02B e 02C estão temporariamente ocupados por palco e vestiário. Quando as fotos de futebol
e EUA aparecerem, elas devem tomar esse lugar: são as duas imagens que mais individualizam o deck,
porque nenhum outro profissional poderia preenchê-las com o mesmo conteúdo.

Os slides 8 e 12 voltaram ao layout de quatro cards em largura cheia, sem coluna de foto: nenhuma
imagem do acervo serve a eles e não fazia sentido reservar espaço vazio. Quando as fotos existirem,
a coluna volta — é uma edição só.

Nos demais slots, foto ainda ausente aparece como painel escuro, não como briefing. O deck está
apresentável a qualquer momento; a tecla `B` revela os briefings quando você for escolher imagens.

---

## Instrumento de triagem

Passe cada foto do acervo por estas dez gavetas antes de escolher qualquer coisa. A classificação
não aparece no deck; ela existe para que a escolha seja por função, não por preferência.

| # | Categoria | O que entra | Onde é usada |
| --- | --- | --- | --- |
| 1 | **Hero / Autoridade** | Wilton sozinho, presença forte, postura, luz e composição acima da média | Slots 01, 13 |
| 2 | **Bodybuilding** | Físico, posing, contexto competitivo | Slots 02A, 13 |
| 3 | **Performance** | Treino, execução, esforço, ambiente esportivo | Slots 05, 03 |
| 4 | **Lifestyle premium** | Carro, arquitetura, academia premium, viagem | Slot 06 |
| 5 | **Profissional** | Wilton como treinador, nutricionista, mentor | Slots 02A, 08 |
| 6 | **Storytelling** | Futebol, Estados Unidos, trajetória, evolução | Slots 02B, 02C |
| 7 | **Humanização** | Natural, próxima, pouco posada | Slot 12 |
| 8 | **Background** | Boa textura, funciona sob overlay escuro | Slots 04, 07, 09, 11 |
| 9 | **Detalhe** | Mãos, relógio, equipamento, carro, pesos, app, computador | Slots 06, 08, 09 |
| 10 | **Descartar** | Desfocada, baixa resolução, repetida, expressão inadequada, fraca | — |

## Critérios de corte

**Entra:** alta resolução · boa iluminação · contraste forte · composição limpa · postura confiante ·
espaço negativo para texto · possibilidade de recorte · coerência com preto, grafite, prata e vermelho.

**Sai:** selfie casual · foto clara demais que quebra a estética · fundo poluído · foto engraçada ·
terceiros roubando atenção · Wilton pequeno demais no quadro · screenshot · terceira foto da mesma
sessão.

**Regra de repetição:** uma foto diferente por slide. A única exceção admitida é a dupla 01 / 13 — e
mesmo aí, prefira outra foto da mesma sessão a repetir o mesmo arquivo.

---

## Tabela de curadoria

Cada linha corresponde a um slot já construído e já cabeado no deck. **Arquivo** traz a foto
escolhida e o nome sob o qual salvá-la em `fotos/`.

### Slide 1 — Hook · slot `01`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | **P03** — academia, parede preta, encostado. Salvar como `fotos/slot-01.jpg`. |
| **Casting** | A foto mais forte do acervo. Corpo inteiro ou meio corpo, academia escura, luz lateral fria, olhar direto na câmera. Postura parada e confiante — não posando, não em execução. |
| **Motivo** | É a primeira coisa que o prospect vê. Precisa produzir "essa pessoa sabe do que está falando" antes de qualquer palavra ser lida. |
| **Recorte** | Vertical 845 × 922 (retrato). Mínimo 1700 × 1850 px. |
| **Posição** | Sangrando à direita, 44% da largura. Texto à esquerda. |
| **Tratamento** | Gradiente `g-left`: preto sólido na borda esquerda → transparente a 58%. Corpo do sujeito no terço direito, longe da headline. |
| **Alternativa nº 2** | **P12** — vestiário, parede preta e faixa vermelha. |

### Slide 2 — Autoridade · slots `02A`, `02B`, `02C`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | **P01** palco (02A) · **P02** troféu (02B) · **P12** vestiário (02C). Salvar como `slot-02a.jpg`, `slot-02b.jpg`, `slot-02c.jpg`. |
| **Casting** | **02A** retrato vertical, Wilton como profissional e atleta, físico apresentado com sobriedade, fundo limpo e escuro. **02B** futebol — foto histórica de campo ou uniforme. **02C** Estados Unidos. |
| **Motivo** | 02A sustenta autoridade presente; 02B e 02C provam a trajetória que os números não provam. As históricas podem ter qualidade técnica inferior — são documento, e isso é legível. |
| **Recorte** | 02A 598 × 734 (mín. 1200 × 1470). 02B/02C 291 × 172, paisagem (mín. 600 × 350). |
| **Posição** | Coluna direita: principal em cima, duas miniaturas lado a lado embaixo. |
| **Tratamento** | Gradiente `g-bottom` nas três, para que as legendas de trajetória fiquem legíveis. |
| **Alternativa nº 2** | **P06** front double biceps para 02A; futebol e EUA quando existirem, para 02B e 02C. |

> Máximo três imagens neste slide. Uma quarta transforma autoridade em álbum de família.

### Slide 3 — Problema real · slot `03`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | **P07** — azulejo, pose lateral, de perfil. Salvar como `fotos/slot-03.jpg`. |
| **Casting** | Contemplativa, não posada. Wilton treinando ou observando — de perfil, olhando para o próprio trabalho. |
| **Motivo** | O slide fala de análise, não de esforço. Uma foto de execução intensa aqui contradiz a copy: o argumento é justamente que intensidade não basta. |
| **Recorte** | Vertical 634 × 922. Mínimo 1270 × 1850 px. |
| **Posição** | Sangrando à direita, 33%. Mais estreita que o slot 01 — aqui a foto acompanha, não domina. |
| **Tratamento** | `g-left`. Manter o rosto acima da metade para não colidir com a barra de citação. |
| **Alternativa nº 2** | **P12** — vestiário. |

### Slide 4 — Os 4 vazamentos · slot `04` (fundo)

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Nenhuma no acervo. Slot opcional — o slide funciona vazio.* |
| **Casting** | Academia muito escura, textura de equipamento, sem sujeito reconhecível. Se houver foto de Wilton analisando celular ou computador, serve — mas fica irreconhecível sob o overlay. |
| **Motivo** | A prioridade deste slide é legibilidade dos quatro cards. A imagem existe para dar profundidade ao preto, não para ser vista. |
| **Recorte** | 1920 × 1080. Mínimo 2400 × 1350 px. |
| **Posição** | Fundo do slide inteiro, atrás de tudo. |
| **Tratamento** | Overlay de 90–95% de preto, dessaturação forte, brilho a 42%. **Slot silencioso:** se ficar vazio, não aparece nada — o slide funciona sem foto. |
| **Alternativa nº 2** | — |

### Slide 5 — Quebra de crenças · slot `05`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | **P10** — azulejo, front lat spread, tensão máxima. Salvar como `fotos/slot-05.jpg`. |
| **Casting** | Wilton treinando pesado. Carga real, esforço visível, sem sorriso. |
| **Motivo** | A imagem precisa **afirmar** "treinar pesado" com força, para que o texto ao lado possa negar que isso baste. Foto fraca aqui enfraquece a quebra de crença. |
| **Recorte** | Vertical 730 × 922 (38% do slide, dentro da faixa de 35–45% pedida). Mínimo 1460 × 1850 px. |
| **Posição** | Sangrando à **esquerda** — inverte o padrão dos slides 1 e 3 e evita que o deck fique monótono. |
| **Tratamento** | `g-right`: preto na borda direita, fundindo com os cards. |
| **Alternativa nº 2** | **P06** — azulejo, front double biceps. |

### Slide 6 — Método 1% · slot `06`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Falta no acervo — prioridade 3. Slot silencioso: o slide está limpo enquanto vazio.* |
| **Casting** | Porsche ou carro premium: detalhe de engenharia, roda, instrumento, linha de carroceria. Se houver foto de Wilton com o carro, tem prioridade. |
| **Motivo** | É o slide do mecanismo, e o carro é a metáfora de precisão e ajuste — nunca de ostentação. Um detalhe de engenharia comunica isso melhor do que o carro inteiro, que lê como status. |
| **Recorte** | 1920 × 1080, sangrando o slide inteiro. Mínimo 2600 × 1460 px. |
| **Posição** | Fundo total. O conteúdo ocupa a esquerda; o assunto da foto deve viver à direita. |
| **Tratamento** | Gradiente diagonal a 100°: preto sólido até 34%, abrindo para 58% de opacidade no centro-direita. Régua de telemetria em vermelho acima do fluxo 4A amarra foto e diagrama à mesma linguagem. |
| **Alternativa nº 2** | — |

### Slide 7 — Ciclo 4A · slot `07` (fundo)

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Nenhuma no acervo. Slot opcional — o slide funciona vazio.* |
| **Casting** | Silhueta, detalhe de academia, ou uma foto sua que funcione em opacidade muito baixa. |
| **Motivo** | O slide mais denso do deck. O diagrama é o produto; qualquer imagem competindo com os quatro cards custa compreensão. |
| **Recorte** | 1920 × 1080. Mínimo 2400 × 1350 px. |
| **Posição** | Fundo total. |
| **Tratamento** | Igual ao slot 04 — overlay 90–95%. Silencioso quando vazio. |
| **Alternativa nº 2** | — |

### Slide 8 — Entrega · slot `08`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Falta no acervo — prioridade 2. O slot exibe o briefing até a foto existir.* |
| **Casting** | Wilton trabalhando: analisando celular ou computador, orientando alguém, conferindo execução. |
| **Motivo** | É o slide do acompanhamento. A foto precisa mostrar **o trabalho**, não o físico — aqui o físico seria argumento errado. Se o acervo tiver um print real da tela do app, ele vale mais que uma foto genérica. |
| **Recorte** | Vertical 614 × 922. Mínimo 1230 × 1850 px. |
| **Posição** | Sangrando à direita, 32%. |
| **Tratamento** | `g-left`. Se a foto tiver tela de celular ou monitor, posicionar para que a tela caia na área clara do gradiente. |
| **Alternativa nº 2** | — |

### Slide 9 — Valor percebido · slot `09` (fundo)

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Deixar vazio, por decisão.* |
| **Casting** | Se usar: abstrato, equipamento, detalhe de físico ou lifestyle premium muito escuro. Nunca rosto. |
| **Motivo** | Este slide precisa parecer documento financeiro. **R$ 5.982,00 é o único elemento que pode chamar atenção.** Qualquer imagem reconhecível o transforma em anúncio e destrói a ancoragem. |
| **Recorte** | 1920 × 1080. |
| **Posição** | Fundo total, opacidade mínima. |
| **Tratamento** | Overlay 90–95%. Recomendação: deixar vazio. |
| **Alternativa nº 2** | — |

### Slide 10 — Investimento principal · slot `10`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | **P06** — azulejo, front double biceps, recorte fechado do peito para cima. Salvar como `fotos/slot-10.jpg`. |
| **Casting** | Retrato vertical sóbrio, fundo escuro e limpo, pouca ação. |
| **Motivo** | Presença premium sem disputar com o preço. O `12x R$ 300` é o maior tipo do deck; a foto é contrapeso, não protagonista. |
| **Recorte** | Vertical 518 × 922 — o slot mais estreito com sujeito. Mínimo 1040 × 1850 px. Enquadramento fechado (peito para cima) funciona melhor nesta largura. |
| **Posição** | Sangrando à direita, 27%. |
| **Tratamento** | `g-left`. Nenhum destaque em vermelho na foto — o vermelho deste slide pertence ao preço. |
| **Alternativa nº 2** | **P01** — palco, recorte fechado. |

### Slide 11 — Condição de entrada · slot `11` (fundo)

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Deixar vazio, por decisão.* |
| **Casting** | Se usar: detalhe discreto de academia ou performance. |
| **Motivo** | Este slide precisa ser o mais limpo do deck. O contraste com o slide 10, que tem foto, já cria hierarquia entre a condição principal e a alternativa — sem precisar de imagem. |
| **Recorte** | 1920 × 1080. |
| **Posição** | Fundo total. |
| **Tratamento** | Overlay 90–95%. Nunca: explosão, etiqueta de desconto, cronômetro, vermelho piscante. |
| **Alternativa nº 2** | — |

### Slide 12 — Compromisso · slot `12`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | *Falta no acervo — prioridade 1. O slot exibe o briefing até a foto existir.* |
| **Casting** | Retrato humano, olhando direto para a câmera. Expressão séria e aberta, sem pose. |
| **Motivo** | É o slide em que Wilton diz o que **não** garante. Contato visual direto é o que faz uma recusa soar como honestidade em vez de ressalva. A foto precisa parecer conversa, não campanha. |
| **Recorte** | Vertical 576 × 922, enquadramento fechado (rosto e ombros). Mínimo 1150 × 1850 px. |
| **Posição** | Sangrando à **esquerda**, 30%. |
| **Tratamento** | `g-right`. Menos contraste que os demais slots, se possível: dureza demais contradiz proximidade. |
| **Alternativa nº 2** | — |

### Slide 13 — Fechamento · slot `13`

| Campo | Especificação |
| --- | --- |
| **Arquivo** | **P11** — azulejo, rear lat spread com braços abertos. Salvar como `fotos/slot-13.jpg`. |
| **Casting** | Uma das três melhores do acervo, **de sessão diferente da do slot 01**. Corpo inteiro, caminhando ou em postura dominante, olhar na câmera. |
| **Motivo** | Precisa dar sensação de movimento e novo nível — não de pose final. Fecha o arco visual aberto no slide 1 sem repeti-lo. |
| **Recorte** | Vertical 787 × 922. Mínimo 1580 × 1850 px. Walking shot funciona melhor que pose estática. |
| **Posição** | Sangrando à direita, 41%. |
| **Tratamento** | `g-left`, mesmo gradiente do slot 01 — a simetria de tratamento entre abertura e fechamento é intencional. |
| **Alternativa nº 2** | **P10** — azulejo, front lat spread. |

---

## Tratamento uniforme

Aplicado por CSS a todos os slots, igual para todos, para que fotos de sessões diferentes convivam
como um conjunto:

| Parâmetro | Valor | Por quê |
| --- | --- | --- |
| Contraste | `1.14` | Pretos mais profundos, coerentes com o fundo `#06070A` |
| Saturação | `0.84` | Dessaturação leve; tons de pele continuam naturais |
| Brilho | `0.88` | Highlights controlados, sem estourar |
| Grão | SVG `fractalNoise`, opacidade `.16`, blend `overlay` | Textura cinematográfica, une sessões diferentes |
| Gradiente | Por slot (`g-left`, `g-right`, `g-bottom`) | Cria o espaço negativo de leitura |
| Fundos | Contraste `1.10`, saturação `0.50`, brilho `0.42` | Some para trás sem virar mancha cinza |

**O que este tratamento não faz, por decisão:** não altera físico, não aumenta músculo, não modifica
rosto, não cria aparência falsa, não estoura HDR, não deixa a pele laranja. É correção de cor, não
retoque. A imagem continua sendo claramente Wilton — se não continuasse, ela deixaria de cumprir a
função de autoridade que justifica estar ali.

## Espaço negativo e hierarquia

Nenhum texto importante cai sobre rosto, físico ou mãos. Em cada slot com sujeito, o gradiente cria
uma faixa de leitura na borda oposta ao sujeito. A ordem de prioridade visual é:

`1. Headline → 2. Mensagem central → 3. Wilton → 4. Dados → 5. Decorativos`

A foto nunca disputa com a copy. Nos slides de preço (9, 10, 11) ela é rebaixada mais um degrau: o
número vem antes de tudo.

## Branding e proporção de cor

`ONEPERCENT1%` aparece no topo esquerdo de todos os 13 slides, `MÉTODO 1%` no rodapé esquerdo,
`WILTON MURILO` no rodapé direito, e a trilha de 13 setores atravessa o topo preenchendo conforme a
apresentação avança. A marca está presente sem nunca ocupar área de conteúdo.

A proporção de cor segue aproximadamente **70% preto/grafite · 20% branco/prata · 10% vermelho**. O
vermelho é energia e marcação — filete de card, acento de número, eixo do slide 3, CTA — nunca campo
de cor.

## Auditoria de identidade

> *"Se eu removesse o nome Wilton Murilo, essa apresentação ainda pareceria genericamente de qualquer coach?"*

Não, e por seis razões construídas de propósito:

1. **Ciclo 4A** — mecanismo nomeado e proprietário, com quatro etapas que só existem aqui.
2. **Método 1%** — conceito central que dá nome ao deck, ao CTA e à frase de fechamento.
3. **Trilha de 13 setores** — a moldura de instrumento é telemetria, e nenhuma delas é decorativa: ela informa posição na call.
4. **Pares de contraste do slide 3** — a estrutura "o que muda em você / o que não muda no plano" é argumento específico deste método.
5. **Bebas Neue condensada em preto profundo com vermelho motorsport** — a combinação é de engenharia automotiva, não de fitness genérico.
6. **Slide 12** — recusar garantia de resultado é posicionamento, e é o oposto do que um coach genérico faz.

O que ainda depende das fotos: **rosto, trajetória e físico**. Os slots 02B e 02C (futebol e Estados
Unidos) são os que mais individualizam o deck, porque são os únicos que nenhum outro profissional
poderia preencher com o mesmo conteúdo. Se o acervo tiver essas duas imagens, elas valem mais para a
identidade do que qualquer foto de treino bem iluminada.

## Como preencher

Uma linha por slot em `deck/_body.html`:

```html
<div class="ph bleed r g-left" data-slot="01"
     style="width:44%;--img:url('fotos/slot-01.jpg');--pos:center 30%">
```

`--pos` ajusta o enquadramento dentro do slot: `center 30%` sobe o recorte, `center 70%` desce.
O briefing de casting e as marcas de enquadramento somem sozinhos. Depois:

```
./deck/build.sh && python3 deck/export.py
```
