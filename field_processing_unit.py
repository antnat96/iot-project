from counterfit_connection import CounterFitConnection
import time
import json
import paho.mqtt.client as mqtt
from counterfit_shims_grove import GroveLightSensor
CounterFitConnection.init('127.0.0.1', 5000)

sensor = GroveLightSensor(1)
position_x = 45
position_z = 45

def handle_fpu_commands(client, userdata, message, position_x, position_z):
    payload = json.loads(message.payload.decode())
    print("handle_fpu_commands:", payload)
    if payload['desired_position_x'] != position_x:
        print("Moving on x-axis...")
        position_x = payload['desired_position_x']
    if payload['desired_position_z'] != position_z:
        print("Moving on z-axis...")
        position_z = payload['desired_position_z']
    print("New position_x: ", position_x)
    print("New position_z: ", position_z)

id = 'csci_ecu_21_ant'
name = id + 'field_processing_unit'
outbound_topic = id + '/fpu_data'
inbound_topic = id + '/fpu_commands'
mqtt_client = mqtt.Client(name)
mqtt_client.connect('35.243.224.151')
mqtt_client.subscribe(inbound_topic)
mqtt_client.loop_start()
mqtt_client.on_message = handle_fpu_commands

while True:
    uv = sensor.light
    data = json.dumps(
        {
        'uv' : uv, 
        'position_x': position_x, 
        'position_z': position_z
        }
    )
    print(data)
    mqtt_client.publish(outbound_topic, data)
    time.sleep(5)