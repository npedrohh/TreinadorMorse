<h1 align="center">
  <img src="https://media.elektor.com/media/catalog/product/cache/9cc822bfc6a57f9729d464b8b5e0e0df/j/o/joy-it-nodemcu-esp32-development-board_front.png" width="300" /><br/>
Treinador de Código Morse <br/>
</h1>

<br/>

## :pushpin: Descrição

Esse projeto visa facilitar o aprendizado do código morse por meio de uma atividade lúdica, em que o usuário deve acertar a tradução da palavra codificada que está sendo transmitida por um LED.

O usuário conecta-se ao Wi-Fi e entra no servidor web criado pelo ESP32, onde ele vai poder inserir a sua resposta e também reiniciar a atividade para tentar novamente.

Após inserir a resposta, o usuário descobrirá se sua tradução está correta pela cor do LED, que irá ficar verde em caso de acerto e vermelho em caso de erro.


<br/>

## :robot: Montagem do dispositivo físico

### Lista de materiais

| Quantidade | Nome | Link para referência |
| --- | --- | --- |
| 1 | ESP32 e cabo USB | https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html |
| 1 | Sensor de Toque Touch Capacitivo TTP223B | https://www.baudaeletronica.com.br/sensor-touch-capacitivo-ttp223b.html |
| 1 | LED RGB Difuso Catodo Comum 5mm | https://www.baudaeletronica.com.br/sensor-de-temperatura-digital-ds18b20.html |
| X | Jumpers variados | --- |
| 1 | Protoboard | --- |

### Lista de conexões

| Componente | Pino da placa |
| --- | --- |
| Sensor de Toque | 4 |
| LED RGB (Vermelho) | 23 |
| LED RGB (Verde) | 22 |
| LED RGB (Azul) | 21 |


### Comportamento dos sensores e atuadores

#### Sensor de Toque TTP223B

Quando o usuário toca com o dedo na região indicada por um silk branco, a saída de sinal do módulo toque fica em nível alto. Seu funcionamento é semelhante a um botão convencional, normalmente com o sinal em baixa, e ao toque, fica alto.

Este Módulo Sensor de Toque Capacitivo TTP223B pode ser instalado em superfícies como materiais não-metálicos, plástico, vidro, pode ser oculto nas paredes, áreas de trabalho e em outras partes de botões. Pode ser empregado em qualquer aplicação como substituto de botões convencionais de toque. (Especificação técnica: https://files.seeedstudio.com/wiki/Grove-Touch_Sensor/res/TTP223.pdf)

#### LED RGB Difuso Catodo Comum

O LED RGB Difuso Catodo Comum nada mais é do que três LED's em um só. Ele é formado por um vermelho (R, de red), um verde (G, de green) e um azul (B, de blue). Associando às cores dos três Leds é possível se obter qualquer cor do espectro visível.


### Circuito

<p align="center">
Figura - Diagrama do circuito<br/>
  <img src="https://github.com/npedrohh/TreinadorMorse/blob/main/src/circuito.jpg" width="400" /><br/>
</p>
<br/>

<br/>

## :electric_plug: Funcionamento do sistema

**Não esqueça: adicione um videozinho do sistema funcionando :)**

Liste informações como:
- requisitos do código
- estrutura de arquivos
- qual o objetivo de cada arquivo/pedaço de código
Não precisa ser muito detalhado, apenas o suficiente para que seu código seja entendível!


<br/>

## ⚙️ Funcionalidades

### Features implementadas

- [x] Capacidade de utilizar uma lista de palavras customizável e de qualquer tamanho, de acordo com a intenção do usuário
- [x] Interação Usuário-Web no treinamento


### Features para incrementar no projeto

- [ ] Feedback para o usuário de quais letras devem ser focadas na memorização, levando em conta as tentativas incorretas
