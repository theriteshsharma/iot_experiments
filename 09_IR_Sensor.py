import RPi.GPIO as GPIO
import time

GPIO_IR = 14
GPIO_BUZZ = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_IR,GPIO.IN)
GPIO.setup(GPIO_BUZZ,GPIO.OUT)
while True:
       ir_in = GPIO.input(GPIO_IR)
       print(ir_in)
       if not ir_in:
           GPIO.output(GPIO_BUZZ,GPIO.HIGH)
       else:
           GPIO.output(GPIO_BUZZ,GPIO.LOW)
       time.sleep(0.5)
       
