import RPi.GPIO as IO
import time
import sys
import os
from time import sleep
import urllib.request

led = 21
IO.setmode(IO.BCM)
IO.setup(led,IO.OUT)
IO.setup(20,IO.IN)
myAPI = "05BMETPJLXN7CXEN"
myDelay = 5 #how many seconds between posting data
print ('starting....')
baseURL='https://api.thingspeak.com/update?api_key=%s' % myAPI
print(baseURL)
while True:
    if(IO.input(20)==True):
        IO.output(21,True)
        print("1")
        urllib.request.urlopen(baseURL +"&field1=%s"%str("1"))
        time.sleep(1)
    else:
        IO.output(21,False)
        print("0")
        urllib.request.urlopen(baseURL +"&field1=%s"%str("0"))
        time.sleep(1)