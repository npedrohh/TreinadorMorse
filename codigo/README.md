<p align="center">
  <img src="https://github.com/npedrohh/TreinamentoMorse/blob/main/src/funcionamento.gif" width="300" /><br/>
  Treinamento de Código Morse<br/>
    <br/>

São dois os arquivos utilizados pelo sistema ESP32:<br/>

├── [boot.py](./boot.py) <br/>
├── [main.py](./main.py)<br/>

Abaixo, há uma breve descrição e explicação de cada trecho de código para cada arquivo.

<br/>


# 🧑‍💻 boot.py

## Descrição

Script executado quando a placa com MicroPython boota.

<br/>

# 🧑‍💻 main.py

## Descrição

Script principal com o programa python que será rodado. Ele é executado após o `boot.py`.

## Passo a passo

Importa as bibliotecas que serão usadas no projeto

```py
import socket
import time
import random
import machine
import network
import esp
import gc
import ure
from machine import Pin, PWM
```

Define 0, 1 e 2 para o nome das cores, de forma que fique mais fácil de escrever e interpretar o código

```py
RED = 0
GREEN = 1
BLUE = 2
```

Inicialização dos pinos que serão usados, e, ao fim, a definição da frequeência do PWM

```py
pwm_pins = [23, 22, 21]
touch = machine.Pin(4, machine.Pin.IN)
pwms = [PWM(Pin(pwm_pins[RED])), PWM(Pin(pwm_pins[GREEN])), PWM(Pin(pwm_pins[BLUE]))]
[pwm.freq(1000) for pwm in pwms]
```

Função que desinicializa o PWM

```py
def deinit_pwm_pins():
    pwms[RED].deinit()
    pwms[GREEN].deinit()
    pwms[BLUE].deinit()
```

Funções que mudam a cor/funcionamento do LED RGB

```py
def desliga_luz():
    pwms[RED].duty_u16(65535)
    pwms[GREEN].duty_u16(65535)
    pwms[BLUE].duty_u16(65535)
def brilha_vermelho():
    pwms[RED].duty_u16(0)
    pwms[GREEN].duty_u16(65535)
    pwms[BLUE].duty_u16(65535) 
def brilha_amarelo():
    pwms[RED].duty_u16(0)
    pwms[GREEN].duty_u16(0)
    pwms[BLUE].duty_u16(65535)
def brilha_verde():
    pwms[RED].duty_u16(65535)
    pwms[GREEN].duty_u16(0)
    pwms[BLUE].duty_u16(65535)
def brilha_azul():
    pwms[RED].duty_u16(65535)
    pwms[GREEN].duty_u16(65535)
    pwms[BLUE].duty_u16(0)
```

Funções que serão utilizadas na execução do código morse: por quantos segundos o "ponto" deve ficar aceso, por quantos segundos o "traço" deve ficar aceso, tempo de espaçamento entre letras e como deve ser feita cada letra, respectivamente

```py
def ponto():
    brilha_amarelo()
    time.sleep(0.4)
    desliga_luz()
    time.sleep(0.4)
def traco():
    brilha_amarelo()
    time.sleep(1.2)
    desliga_luz()
    time.sleep(0.4) 
def espaco_letras():
    time.sleep(1.2)
def escreve_letra(letra):
    if(letra=='a'):
        ponto()
        traco()
        espaco_letras()
    if(letra=='b'):
        traco()
        ponto()
        ponto()
        ponto()
        espaco_letras()
    if(letra=='c'):
        traco()
        ponto()
        traco()
        ponto()        
        espaco_letras()
    [...]
```

Função que será utilizada para extrair a resposta do usuário pelo site

```py
def extract_sugestao(self, request):
        match = ure.search("sugestao=(.*?) ", request)
        if match:
            return match.group(1).replace("+", " ")
        else:
            return None
```

Funções que funcionam em sequência: primeiramente, a função `escolher_palavra()` escolherá a palavra a ser codificada e que o usuário deve acertar. Em seguida, a função "morse" irá enviar a mensagem codificada em forma de luz para o usuário. Por fim, a função "checar" irá verificar se a resposta enviada pelo usuário está correta ou não, e, em caso positivo, fará o LED RGB brilhar na cor verde, e, em caso negativo, fará o LED RGB brilhar na cor vermelha.

```py
def escolher_palavra(self):
        palavras = ["bioma","drama","rumor","morna","fundo","cobre","tiros","lenha","morte","ponte","zebra","termo","furia","censo","falar","marte","setor","corte","firme","bomba","bruno","aline","pedro", "linux","papel", "pedra"]
        tamanho = len(palavras)
        escolha = random.randint(0, tamanho-1)
        self.palavra_escolhida = palavras[escolha]
        
    def morse(self, palavra_escolhida):         
        desliga_luz()
        while touch.value() == 0:
             time.sleep(1)
        for letra in palavra_escolhida:
            time.sleep(1)
            escreve_letra(letra)
            
    def checar(self, sugestao):
                print (sugestao)
                result = sugestao == self.palavra_escolhida
                if result:
                    brilha_verde()
                else:
                    brilha_vermelho()
```

Inicializa a conexão Wi-Fi

```py
def __init__(self):
        esp.osdebug(None)
        gc.collect()
        self.station = network.WLAN(network.STA_IF)
        self.station.active(True)
        self.palavra_escolhida = None
```

Estabelece a conexão Wi-Fi com a rede especificada pelo SSID e senha fornecidos como parâmetros

```py
def connect(self, ssid, password):
        self.station.connect(ssid, password)
        while self.station.isconnected() == False:
          pass
        print('Connection successful')
        print(self.station.ifconfig())
```

Retorna uma página HTML que será exibida quando o cliente acessar o endereço do servidor

```py
def web_page(self):
        html = """<!DOCTYPE html><html><head><title>Treinamento de Morse</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{font-family:Helvetica,Arial,sans-serif;
        display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;margin:0;background-color:#f2f2f2}h1{color:#0F3376;margin-top:0}form{display:flex;flex-direction:column;
        align-items:center}textarea{width:80%;min-height:100px;padding:10px;font-size:18px;border-radius:4px;border:1px solid #ccc;margin-bottom:10px}.button{display:inline-block;background-color:#000000;border:none;
        border-radius:4px;color:white;padding:16px 40px;text-decoration:none;font-size:24px;margin-top:10px;cursor:pointer}.button:hover{background-color:#333333}.button2{background-color:#4286f4}.restart-button{display:none;margin-top:20px}</style>
        <script>function showRestartButton(){document.getElementById("restartButton").style.display="inline-block"}</script></head><body><h1>Treinamento de Morse</h1><form action="/" method="get"><textarea minlength="1" maxlength="255" name="sugestao" placeholder="Digite sua resposta aqui"></textarea>
        <button class="button button2" type="submit" onclick="showRestartButton()">Enviar</button></form><button id="restartButton" class="button" onclick="location.reload()">Reiniciar</button></body></html>""" 
        return html
```

A função `start()` é responsável por iniciar o servidor socket, aguardar a conexão de um cliente, receber as requisições HTTP, enviar a página web como resposta inicial e, em seguida, iniciar o processo de exibição do código morse e verificação das respostas

Inicialização do socket vinculado ao endereço IP local e à porta 3000. Em seguida, há a definição de um máximo de 2 conexões simultâneas

```py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3000))
s.listen(2)
```

O servidor, então, entra em um loop infinito para continuar aceitando conexões, lidando com requisições e executando o trabalho de escolher uma nova palavra aleatória e codificá-la em morse

Por fim, a "respostaFinal" é declarada como 0 se o usuário tiver enviado uma resposta ou 1 se não tiver enviado nenhuma resposta, por exemplo, caso seja sua primeira interação com o site. A função dessa variável será explicada no próximo passo

```py
 while True:
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            request = str(request)
            print('Content = %s' % request)
            self.escolher_palavra()
            response = self.web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
            self.morse(self.palavra_escolhida)
            respostaFinal = None == self.extract_sugestao(request)
```

O servidor entra em um loop, do qual apenas sairá após o usuário enviar uma resposta. Isso é feito para que uma requisição sem resposta não seja compreendida pelo programa como uma resposta errada, o que faria o LED RGB brilhar na cor vermelha

```py
while respostaFinal:
                conn, addr = s.accept()
                print('Got a connection from %s' % str(addr))
                request = conn.recv(1024)
                request = str(request)
                print('Content = %s' % request)
                response = self.web_page()
                conn.send('HTTP/1.1 200 OK\n')
                conn.send('Content-Type: text/html\n')
                conn.send('Connection: close\n\n')
                conn.sendall(response)
                conn.close()
                respostaFinal = None == self.extract_sugestao(request)
```

Por fim, é checado se a resposta enviada está correta ou não

```py
self.checar(self.extract_sugestao(request))
```

Função principal, que dá a ordem de execução do código, e onde deve ser colocado o nome e a senha da rede que o ESP32 irá se conectar

```py
def main():
    server = ESPServer()
    server.connect("NomeDaRede", "SenhaDaRede")
    server.start()
```

Permite que o código seja executado apenas quando o módulo é executado diretamente como um programa principal

```py
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        deinit_pwm_pins()
```
