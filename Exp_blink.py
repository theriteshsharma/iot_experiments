import RPi.GPIO as GPIO
import time
LedPin = 14    # LED PIN

#Setting up Pins
GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.output(LedPin, GPIO.HIGH) # Turn ON led

# Main Loop
for i in range(10):
  GPIO.output(LedPin, GPIO.HIGH)  # led on
  time.sleep(1)
  GPIO.output(LedPin, GPIO.LOW) # led off
  time.sleep(1)
  print("I am blinking")


# Clean up
GPIO.output(LedPin, GPIO.LOW)   # led off
GPIO.cleanup()                  # Release resource

