import json
import time
import paho.mqtt.client as mqtt
from os import path
import csv
from datetime import datetime

id = 'csci_ecu_21_ant'
name = id + 'analytics_engine'
inbound_topic = id + '/fpu_data'
outbound_topic = id + '/fpu_commands'
mqtt_server = mqtt.Client(name)
mqtt_server.connect('35.243.224.151')
mqtt_server.subscribe(inbound_topic)
mqtt_server.loop_start()
file_name = 'fpu_data.csv'
fieldnames = ['date', 'wattage', 'x_pos']
curr_wattage = 0
last_wattage = 0

def handle_fpu_data(client, userdata, message):
    global curr_wattage
    global last_wattage
    inbound = json.loads(message.payload.decode())
    curr_wattage = inbound['wattage']
    print(curr_wattage)
    outbound_data = {}
    shouldPublish = False
    # If difference is greater than 100 watts between last wattage and current wattage, there is
    # probably just some cloud cover and we don't want the system to move yet
    # But if the difference is small and the last wattage report was higher, we probably need to move to keep up with the sun
    if curr_wattage < last_wattage and (abs(curr_wattage - last_wattage) < 100 or last_wattage == 0):
        outbound_data = json.dumps(
            {
            'desired_position_x': inbound['position_x'] + 2, 
            }
        )
        shouldPublish = True
        
    if shouldPublish == True:
        mqtt_server.publish(outbound_topic, outbound_data)
    last_wattage = curr_wattage
    with open(file_name, mode='a') as wattage_file:        
        wattage_writer = csv.DictWriter(wattage_file, fieldnames=fieldnames)
        wattage_writer.writerow({'date' : datetime.now().astimezone().replace(microsecond=0).isoformat(), 'wattage' : curr_wattage, 'x_pos':  inbound['position_x'] })

mqtt_server.on_message = handle_fpu_data

if not path.exists(file_name):
    with open(file_name, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

while True:
    time.sleep(2)