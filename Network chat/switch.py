import RPi.GPIO as GPIO
import time

SWITCH = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN)

while True:
	if (GPIO.input(SWITCH)):
		print "ON"
	else:
		print "OFF"
	time.sleep(0.5)
  
# note: run with:
#   sudo python switch.py


