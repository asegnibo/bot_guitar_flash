<h1 align="center">🎸 Guitar Flash Bot 🎸</h1>

O **bot_guitar_flash** é um bot automatizado para o jogo [Guitar Flash 3](https://guitarflash3.com/) , que detecta as notas na tela e simula o pressionamentos das teclas correspondentes a cada nota no jogo. 

## 🔧 Recursos

## 👷🏽‍♂️Arquitetura

Abaixo estão os diagramas ilustrando o fluxo da aplicação e sua arquitetura:



AreaJogo => Define a área da tela onde o jogo é capturado.

Tecla	=> Representa cada tecla usada no jogo (com posição e nome).

FaixaHSV =>	Define os valores HSV para detectar notas.

Execution =>	Representa uma execução completa do bot.

EventoNota =>	Registra cada tentativa de detecção de nota durante a sessão.

LogTecla =>	Registra quando cada tecla foi pressionada ou solta


