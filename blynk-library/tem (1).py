##sudo pip3 install Adafruit_DHT
import Adafruit_DHT
import time
import BlynkLib


sensor=Adafruit_DHT.DHT11
blynk = BlynkLib.Blynk(' yFFAB0H5D476sfYy6yU026kpO8h9-4op')
 
gpio=21
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)



# Initialize Blynk

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    print('Current V0 value: {}'.format(value))

@blynk.VIRTUAL_READ(1)
def my_read_handler():
    if humidity is not None and temperature is not None:
      print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
      blynk.virtual_write(1,humidity)
      blynk.virtual_write(0,temperature)

    else:
      print('Failed to get reading. Try again!')
    time.sleep(3)
    

while True:
    my_read_handler()
    blynk.run()
    time.sleep(1)
