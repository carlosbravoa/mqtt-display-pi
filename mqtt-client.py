#########################################
#
# MQTT Client
# Original source: http://www.steves-internet-guide.com/into-mqtt-python-client/
#
#########################################

import paho.mqtt.client as mqtt
import time

def message_arrived(client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

MQTT_server="192.168.1.9" 
topic = "message_display"

client = mqtt.Client("Pi Client")
client.on_message=message_arrived

print("Connecting to MQTT Client...")
client.connect(MQTT_server) 

client.loop_start()

print("Subscribing to topic",topic)
client.subscribe(topic)
#print("Publishing message to topic",topic)
#client.publish("house/bulbs/bulb1","OFF")

while(True):
  #nothing, just wait
  time.sleep(10)


