import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import cayenne.client

# assignment specific
shouldControlTemperature = True

# pin info
pinYellowLed = 20
pinRedLed = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinRedLed, GPIO.OUT)
GPIO.setup(pinYellowLed, GPIO.OUT)
sensor = Adafruit_DHT.DHT11
sensorPin = 2 

# mqtt for mydevices
mqttUser = '770f66b0-c6f4-11eb-8779-7d56e82df461'
mqttPassword = '4abd86fa3423f56ceec0000bfee2c260da84d88a'
clientId = '0eb6f2d0-c6f5-11eb-b767-3f1a8f1211ba'
server = 'mqtt.mydevices.com'
port = 1883
channelZero = '0'
channelOne = '1'
channelTwo = '3'
temperatureChannel = 'v1/'+mqttUser+'/things/'+clientId+'/data/'+channelZero
humidityChannel = 'v1/'+mqttUser+'/things/'+clientId+'/data/'+channelOne
subscribeButton = 'v1/'+mqttUser+'/things/'+clientId+'/cmd/'+channelTwo
publishButton = 'v1/'+mqttUser+'/things/'+clientId+'/data/'+channelTwo

# cayenne mqtt client
client = cayenne.client.CayenneMQTTClient()
client.begin(mqttUser, mqttPassword, clientId)

# function to receive message from mydevice with cayenne mqtt
def message(msg):
    if msg.value == '1':
        print('should control temperature')
        shouldControlTemperature = True
    else:
        print('should not control temperature anymore')
        shouldControlTemperature = False

# Receiving information
client.on_message = message

# loop
for i in range(1, 61):
   client.loop()
   umid, temp = Adafruit_DHT.read_retry(sensor, sensorPin);
   if umid is not None and temp is not None:

     if shouldControlTemperature:
        client.celsiusWrite(temperatureChannel, temp)
        client.celsiusWrite(humidityChannel, umid)
        time.sleep(3)
        print('Should control temp?')
        print(shouldControlTemperature)
        if (temp < 21 or umid < 74) and shouldControlTemperature == 1:
            print("Ligando led amarelo, temperatura acima/igual de 21 graus celsius")
            GPIO.output(pinYellowLed, GPIO.LOW)
            GPIO.output(pinRedLed, GPIO.HIGH)
        else:
            print("Ligando led vermelho, temperatura abaixo de 21 graus celsius")
            GPIO.output(pinRedLed, GPIO.LOW)
            GPIO.output(pinYellowLed, GPIO.HIGH)   

        time.sleep(2)
   else:
     print("Falha ao ler dados do DHT11 !!!")


