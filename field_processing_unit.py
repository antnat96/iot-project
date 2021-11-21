from counterfit_connection import CounterFitConnection
import time
import json
import paho.mqtt.client as mqtt
from counterfit_shims_grove import GroveLightSensor
CounterFitConnection.init('127.0.0.1', 5000)

id = 'csci_ecu_21_ant'
name = id + 'field_processing_unit'
topic = id + '/data'
mqtt_client = mqtt.Client(name)
mqtt_client.connect('35.243.224.151')
mqtt_client.loop_start()
sensor = GroveLightSensor(1)

while True:
    light = sensor.light
    data = json.dumps({'light' : light})
    print(data)
    mqtt_client.publish(topic, data)
    time.sleep(5)