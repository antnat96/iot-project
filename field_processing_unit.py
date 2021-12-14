from counterfit_connection import CounterFitConnection
import time
import json
import paho.mqtt.client as mqtt
from counterfit_shims_grove import GroveLightSensor
from counterfit_shims_grove.grove_relay import GroveRelay
CounterFitConnection.init('127.0.0.1', 5000)

sensor = GroveLightSensor(1)
relay = GroveRelay(2)
position_x = 45

def handle_fpu_commands(client, userdata, message):
    global position_x
    payload = json.loads(message.payload.decode())
    if payload['desired_position_x'] != position_x:
        print("Moving from", position_x, "degrees to", payload['desired_position_x'], "degrees")
        relay.on()
        time.sleep(2)
        position_x = payload['desired_position_x']
        print("Moved to", position_x, "degrees!")
        relay.off()

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
    wattage = sensor.light
    outbound_data = json.dumps(
        {
        'wattage' : wattage, 
        'position_x': position_x, 
        }
    )
    mqtt_client.publish(outbound_topic, outbound_data)
    time.sleep(5)