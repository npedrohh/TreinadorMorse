<p align="center">
  <img src="https://media.elektor.com/media/catalog/product/cache/9cc822bfc6a57f9729d464b8b5e0e0df/j/o/joy-it-nodemcu-esp32-development-board_front.png" width="300" /><br/>
  Treinamento de Código Morse<br/>
    <br/>

São dois os arquivos utilizados pelo sistema ESP32:<br/>

├── [boot.py](./boot.py) <br/>
├── [main.py](./main.py)<br/>

Abaixo, há uma breve descrição e explicação de cada trecho de código para cada arquivo.

<br/>


# 🧑‍💻 boot.py

## Descrição

Script executado quando a placa com MicroPython boota. Serve para definir configurações da aplicação, como, por exemplo, quais pinos serão usados para os sensores, importação de bibliotecas e conexão da placa ao wi-fi.

<br/>

# 🧑‍💻 main.py

## Descrição

Script principal com o programa python que será rodado. Ele é executado após o `boot.py`. Serve como servidor para receber requisições em suas funções pela página web.

## Passo a passo
