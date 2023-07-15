import socket
import time
import random
import machine
import network
import esp
import gc
import ure
from machine import Pin, PWM

# RGB
RED = 0
GREEN = 1
BLUE = 2

# Inicializar os pinos
pwm_pins = [23, 22, 21]
touch = machine.Pin(4, machine.Pin.IN)
pwms = [PWM(Pin(pwm_pins[RED])), PWM(Pin(pwm_pins[GREEN])), PWM(Pin(pwm_pins[BLUE]))]

# Definir a frequência do PWM
[pwm.freq(1000) for pwm in pwms]

# Desinicializar os pinos PWM
def deinit_pwm_pins():
    pwms[RED].deinit()
    pwms[GREEN].deinit()
    pwms[BLUE].deinit()

# Funções do LED RGB
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
    
# Funções do código morse
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
    if(letra=='d'):
        traco()
        ponto()
        ponto()
        espaco_letras()
    if(letra=='e'):
        ponto()
        espaco_letras()
    if(letra=='f'):
        ponto()
        ponto()
        traco()
        ponto()
        espaco_letras()
    if(letra=='g'):
        traco()
        traco()
        ponto()        
        espaco_letras()       
    if(letra=='h'):
        ponto()
        ponto()
        ponto()
        ponto()
        espaco_letras()
    if(letra=='i'):
        ponto()
        ponto()
        espaco_letras()
    if(letra=='j'):
        ponto()
        traco()
        traco()
        traco()
        espaco_letras()
    if(letra=='k'):
        traco()
        ponto()
        traco()
        espaco_letras()
    if(letra=='l'):
        ponto()
        traco()
        ponto()
        ponto()
        espaco_letras()
    if(letra=='m'):
        traco()
        traco()
        espaco_letras()
    if(letra=='n'):
        traco()
        ponto()
        espaco_letras()    
    if(letra=='o'):
        traco()
        traco()
        traco()
        espaco_letras()
    if(letra=='p'):
        ponto()
        traco()
        traco()
        ponto()
        espaco_letras()  
    if(letra=='q'):
        traco()
        traco()
        ponto()
        traco()
        espaco_letras()
    if(letra=='r'):
        ponto()
        traco()
        ponto()
        espaco_letras()      
    if(letra=='s'):
        ponto()
        ponto()
        ponto()
        espaco_letras()      
    if(letra=='t'):
        traco()
        espaco_letras()      
    if(letra=='u'):
        ponto()
        ponto()
        traco()
        espaco_letras()
    if(letra=='v'):
        ponto()
        ponto()
        ponto()
        traco()
        espaco_letras()
    if(letra=='w'):
        ponto()
        traco()
        traco()
        traco()
        espaco_letras()
    if(letra=='x'):
        traco()
        ponto()
        ponto()
        traco()
        espaco_letras() 
    if(letra=='y'):
        traco()
        ponto()
        traco()
        traco()
        espaco_letras()
    if(letra=='z'):
        traco()
        traco()
        ponto()
        ponto()
        espaco_letras()

# Servidor
class ESPServer:
    def extract_sugestao(self, request):
        match = ure.search("sugestao=(.*?) ", request)
        if match:
            return match.group(1).replace("+", " ")
        else:
            return None
        
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

    def __init__(self):
        esp.osdebug(None)
        gc.collect()
        self.station = network.WLAN(network.STA_IF)
        self.station.active(True)
        self.checador = 1
        self.palavra_escolhida = None
    def connect(self, ssid, password):
        self.station.connect(ssid, password)
        while self.station.isconnected() == False:
          pass
        print('Connection successful')
        print(self.station.ifconfig())
    def web_page(self):
        html = """<!DOCTYPE html><html><head><title>Treinamento de Morse</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{font-family:Helvetica,Arial,sans-serif;
        display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;margin:0;background-color:#f2f2f2}h1{color:#0F3376;margin-top:0}form{display:flex;flex-direction:column;
        align-items:center}textarea{width:80%;min-height:100px;padding:10px;font-size:18px;border-radius:4px;border:1px solid #ccc;margin-bottom:10px}.button{display:inline-block;background-color:#000000;border:none;
        border-radius:4px;color:white;padding:16px 40px;text-decoration:none;font-size:24px;margin-top:10px;cursor:pointer}.button:hover{background-color:#333333}.button2{background-color:#4286f4}.restart-button{display:none;margin-top:20px}</style>
        <script>function showRestartButton(){document.getElementById("restartButton").style.display="inline-block"}</script></head><body><h1>Treinamento de Morse</h1><form action="/" method="get"><textarea minlength="1" maxlength="255" name="sugestao" placeholder="Digite sua resposta aqui"></textarea>
        <button class="button button2" type="submit" onclick="showRestartButton()">Enviar</button></form><button id="restartButton" class="button" onclick="location.reload()">Reiniciar</button></body></html>""" 
        return html
    
    def start(self):
        # Inicialização do socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 3000))
        s.listen(2)
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
            self.checar(self.extract_sugestao(request))

def main():
    server = ESPServer()
    server.connect("morse", "04130211")
    server.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        deinit_pwm_pins()
