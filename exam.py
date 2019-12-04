#!/usr/bin/python3

import RPi.GPIO as GPIO
import sys
import time
import Adafruit_DHT
import http.client as http
import urllib
import json

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#MCS client

deviceid = "DLEIm9E6"

deviceKey = "uui6LEb5yO6quvg5"

def post_to_mcs(payload):
	headers = {"Content-type":"application/json","deviceKey":deviceKey}
	not_connected = 1
	while(not_connected):
		try:
			conn = http.HTTPConnection("api.mediatek.com:80")
			conn.connect()
			not_connected = 0
		except(http.HTTPException) as ex:
			print("Error:%s"%ex)
			time.sleep(10)
	conn.request("POST","/mcs/v2/devices/"+deviceid+"/datapoints",json.dumps(payload),headers)

	response = conn.getresponse()
	print(response.status,response.reason,json.dumps(payload),time.strftime("%c"))
	data = response.read()
	conn.close()	

# Parse command line parameters.

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

while True:
	SwitchStatus = GPIO.input(24)

	print(SwitchStatus)
	payload = {"datapoints":[{"dataChnId":"Switch","values":{"value":SwitchStatus}}]} 
	post_to_mcs(payload)
	time.sleep(5)
