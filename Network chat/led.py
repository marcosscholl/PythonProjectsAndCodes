import RPi.GPIO as GPIO
import time

LED = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
	GPIO.output(LED, True)
	time.sleep(1)
	GPIO.output(LED, False)
	time.sleep(1)
  
# note: run with:
#   sudo python led.py

