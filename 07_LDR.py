import RPi.GPIO as GPIO
import time
import sys

GPIO_LDR = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LDR,GPIO.IN)
while True:
       print(GPIO.input(GPIO_LDR))
       time.sleep(0.5)
       