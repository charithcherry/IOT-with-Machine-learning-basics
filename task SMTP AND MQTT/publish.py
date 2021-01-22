#pip install paho-mqtt
import paho.mqtt.client as mqtt

while(1):
    
    client = mqtt.Client()
    client.connect("broker.mqtt-dashboard.com",1883,60)
    client.publish("1234567890","Hi..everyone this is Charith");
    client.disconnect();

 
