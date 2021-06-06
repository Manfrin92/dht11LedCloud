import paho.mqtt.client as mqtt
import time

mqttUser = '770f66b0-c6f4-11eb-8779-7d56e82df461'
mqttPassword = '4abd86fa3423f56ceec0000bfee2c260da84d88a'
clientId = '0eb6f2d0-c6f5-11eb-b767-3f1a8f1211ba'
server = 'mqtt.mydevices.com'
port = 1883

channelOne = '0'
channelThree = '2'

firstChannel = 'v1/'+mqttUser+'/things/'+clientId+'/data/'+channelOne
subscribeButton = 'v1/'+mqttUser+'/things/'+clientId+'/cmd/'+channelThree
publishButton = 'v1/'+mqttUser+'/things/'+clientId+'/data/'+channelThree

client = mqtt.Client(clientId)
client.username_pw_set(mqttUser, mqttPassword)
client.connect(server, port)

def message(client, userData, msg):
    # print('topic: ', msg.topic)
    # print('payload: ', msg.payload.decode('utf-8'))
    payload = msg.payload.decode('utf-8').split(',')[1]
    client.publish(publishButton, payload[1])

# Receiving information
client.on_message = message
client.subscribe(subscribeButton)

client.loop_start()

for i in range(1, 16):
    # Sending information
    client.publish(firstChannel, 0+i)
    time.sleep(2)

