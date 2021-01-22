#import RPi.GPIO as GPIO
import time
import sys
import os
from time import sleep
import urllib.request
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(21,GPIO.OUT)
#GPIO.setup(20,GPIO.IN)
#setup our API and delay
myAPI = "HCDVYQE81JMWBAP9"
myDelay = 5 #how many seconds between posting data

print ('starting....')
baseURL='https://api.thingspeak.com/update?api_key=%s' % myAPI
print(baseURL)

while True:
    for i in range(0,101,20):
        print(i)
        urllib.request.urlopen(baseURL +"&field1=%s"%str(i))
        time.sleep(15)   
                 
    for i in range(100,0,-20):       
        print(i)
        urllib.request.urlopen(baseURL +"&field1=%s"%str(i))
        time.sleep(15)
          
    #urllib.request.urlopen(baseURL +"&field1=%s"%str(distance))
    #urllib.request.urlopen(baseURL +"&field3=%s"%str(i))
    
    #sleep(int(myDelay))
 
