import RPi.GPIO as GPIO
import time
import Adafruit_DHT

LED_PIN_YELLOW = 20
LED_PIN_RED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setup(LED_PIN_YELLOW, GPIO.OUT)
sensor = Adafruit_DHT.DHT11
pino_sensor = 2
 
print ("*** Lendo os valores de temperatura e umidade");
 
while(1):
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
   # Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n").format(temp, umid);
     if temp >= 22:
         print("Piscando led amarelo")
         GPIO.output(LED_PIN_RED, GPIO.LOW)
         GPIO.output(LED_PIN_YELLOW, GPIO.HIGH)
         time.sleep(1)
         GPIO.output(LED_PIN_YELLOW, GPIO.LOW)
     else:
         print("Piscando led vermelho")
         GPIO.output(LED_PIN_YELLOW, GPIO.LOW)
         GPIO.output(LED_PIN_RED, GPIO.HIGH)
         time.sleep(1)
         GPIO.output(LED_PIN_RED, GPIO.LOW)
    

     time.sleep(2)
   else:
     print("Falha ao ler dados do DHT11 !!!")
