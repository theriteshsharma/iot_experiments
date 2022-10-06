import RPi.GPIO as GPIO
import paho.mqtt.client as paho

#from urllib.parse import urlparse
import urllib.parse as urlparse
import time
import os,sys

# initial Setup
GPIO.setmode(GPIO.BCM) 
# Pin Numbers
GPIO_TRIG = 14 
GPIO_ECHO = 18
GPIO_LED = 16

GPIO.setup(GPIO_TRIG, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED,GPIO.OUT)

def get_distance():

    # Trigger Signal 
    GPIO.output(GPIO_TRIG, GPIO.LOW) 
    time.sleep(2) 
    GPIO.output(GPIO_TRIG, GPIO.HIGH) 

    time.sleep(0.00001) 

    GPIO.output(GPIO_TRIG, GPIO.LOW) 

    # Check for Received Signal
    while GPIO.input(GPIO_ECHO)==0: 
        start_time = time.time() 
    while GPIO.input(GPIO_ECHO)==1: 
        Bounce_back_time = time.time() 
    
    # Calculate Pulse Duration from transmision to receving
    pulse_duration = Bounce_back_time - start_time 

    #Calculate distance using speed of sound
    distance = round(pulse_duration * 17150, 2)
    return distance


GPIO.setwarnings(False)
# Setting up LED On Distance
LED_PIN = 16
GPIO.setup(LED_PIN,GPIO.OUT)   
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

# Mqtt Code
def on_connect(self, mosq, obj, rc):
        self.subscribe("led", 0)
    
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print(msg.payload)
    
    #while (True):
    if(msg.payload == b'off'):# Run forever
        print ("LED off")
        GPIO.output(LED_PIN, GPIO.LOW) # Turn on
   # LED OFF

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))



mqttc = paho.Client()                        # object declaration
# Assign event callbacks
mqttc.on_message = on_message                          # called as callback
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883') 
url = urlparse.urlparse(url_str)
mqttc.connect(url.hostname, url.port)

# Main Loop
while True:
    dist = get_distance()
    if dist < 10:
        GPIO.output(GPIO_LED,GPIO.HIGH)
        time.sleep(5)
        rc = 0
        while True:
            while rc == 0:
                import time   
                rc = mqttc.loop()
    print (f"Distance: {dist} cm")
    time.sleep(0.1)

# Cleanup
GPIO.cleanup()