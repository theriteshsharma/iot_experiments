import RPi.GPIO as GPIO 
from time import sleep
#Setting up Pins

GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(14, GPIO.HIGH) # Turn on
 sleep(.1) # 
 GPIO.output(14, GPIO.LOW) # Turn off
 sleep(.1) # 

GPIO.cleanup()