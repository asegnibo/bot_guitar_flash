<h1 align="center">🎸 Guitar Flash Bot 🎸</h1>

O **bot_guitar_flash** é um bot automatizado, feito em python, para o jogo [Guitar Flash 3](https://guitarflash3.com/) , que detecta as notas na tela e simula o pressionamentos das teclas correspondentes a cada nota no jogo. 

## 🔧 Visão Geral

O bot utiliza as bibliotecas:

- `mss` para captura de tela em tempo real.
- `OpenCV` para conversão e análise de imagem no espaço de cores HSV.
- `keyboard` para simular pressionamento de teclas.

## 👷🏽‍♂️Arquitetura

Abaixo estão os diagramas ilustrando o fluxo da aplicação e sua arquitetura.

<img src="images/diagrama1.png" width= "900">


- **`AreaJogo`**  
  Define a área da tela onde o jogo é capturado.

- **`Tecla`**  
  Representa cada tecla usada no jogo, com sua posição na tela e descrição.

- **`FaixaHSV`**  
  Define os valores HSV utilizados para detectar as notas visuais na tela.

- **`Execucao`**  
  Representa uma execução completa do bot (início, fim, FPS, total de notas, etc.).

- **`EventoNota`**  
  Registra cada tentativa de detecção de uma nota durante a execução, com dados de cor HSV e momento.

- **`LogTecla`**  
  Registra os momentos em que cada tecla foi pressionada ou solta durante a execução.

## 🚀Como usar

1. Clonar repositório:
```bash
git clone https://github.com/asegnibo/bot_guitar_flash.git
```
2. Baixar bibliotecas necessárias
```bash
pip install mss
```
```bash
pip install opencv-python
```
```bash
pip install numpy
```
```bash
pip install keyboard
```
3. Ajuste na área do jogo: Você deve inserir os índices (top, left, width e height) na variável **`game_area`**. Se necessário, ajuste essas coordenadas conforme seu monitor, obtendo os índices utilizando o arquivo *cursor_position*

4. Configuração das teclas: Por padrão, o jogo utiliza as teclas (a, s, j, k, l). Caso queira alterar, basta alterar em **`keys`**.

6. Selecionar os circulos de identificação. Utilize o arquivo py *cursor_position* para configurar para sua tela conforme abaixo:
7.  



