import RPi.GPIO as GPIO
import time

GPIO_LDR = 14
GPIO_BUZZ = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LDR,GPIO.IN)
GPIO.setup(GPIO_BUZZ,GPIO.OUT)
while True:
       ldr_in = GPIO.input(GPIO_LDR)
       print(ldr_in)
       if ldr_in:
           GPIO.output(GPIO_BUZZ,GPIO.HIGH)
       else:
           GPIO.output(GPIO_BUZZ,GPIO.LOW)
       time.sleep(0.5)
       