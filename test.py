#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
	switch = GPIO.input(24)
	if switch == 1:
		print("switch on")
	else:
		print("switch off")	
	time.sleep(5)	
GPIO.cleanup()
