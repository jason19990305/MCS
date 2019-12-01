#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

while True:
	GPIO.output(4,1)
	time.sleep(1)
	GPIO.output(4,0)
	time.sleep(0.5)	
GPIO.cleanup()
