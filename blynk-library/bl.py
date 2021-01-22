import BlynkLib
import time
# Initialize Blynk
blynk = BlynkLib.Blynk('yFFAB0H5D476sfYy6yU026kpO8h9-4op')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    print('Current V0 value: {}'.format(value))

@blynk.VIRTUAL_READ(1)
def my_read_handler():
    ## this widget will show some time in seconds..
##    blynk.virtual_write(2, int(time.time()))
    value1="1"
    value2="96"
    blynk.virtual_write(0,value1)
    blynk.virtual_write(1,value2)

while True: 
    blynk.run()
