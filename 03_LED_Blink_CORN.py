import RPi.GPIO as GPIO
import time
LedPin = 11    # Pin For LED

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.output(LedPin, GPIO.HIGH) # Turn ON led

# Main Loop
while True:
    GPIO.output(LedPin, GPIO.HIGH) # LED on
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW) # LED off
    time.sleep(1)

#Cleanup 
GPIO.output(LedPin, GPIO.LOW)   # led off
GPIO.cleanup()                  # Release resource
