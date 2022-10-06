from time import sleep
import os,sys
import RPi.GPIO as GPIO
import paho.mqtt.client as paho

import urllib.parse as urlparse

#initial Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN = 14  #define LED pin
GPIO.setup(LED_PIN,GPIO.OUT)   # Set pin function as output
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)

def on_connect(self, mosq, obj, rc):
        self.subscribe("led", 0)
    
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print(msg.payload)
    if(msg.payload == b'on'):    
        #print ("LED on")      
        GPIO.output(LED_PIN,GPIO.HIGH)  #LED ON
    else:
        #print ("LED off")
        GPIO.output(LED_PIN,GPIO.LOW)   # LED OFF

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))



mqttc = paho.Client()                     
# Assign event callbacks
mqttc.on_message = on_message                         
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe



url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883') 
url = urlparse.urlparse(url_str)
mqttc.connect(url.hostname, url.port)

# Main Loop
rc = 0
while True:
    while rc == 0:
        import time   
        rc = mqttc.loop()
        #time.sleep(0.5)
    print("rc: " + str(rc))
