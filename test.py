#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
	SwitchStatus = GPIO.input(24)
	print(SwitchStatus)
