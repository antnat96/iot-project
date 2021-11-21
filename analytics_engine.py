import json
import time
import paho.mqtt.client as mqtt
from os import path
import csv
from datetime import datetime

id = 'csci_ecu_21_ant'
name = id + 'analytics_engine'
topic = id + '/fpu_data'
mqtt_client = mqtt.Client(name)
mqtt_client.connect('35.243.224.151')
mqtt_client.subscribe(topic)
mqtt_client.loop_start()
file_name = 'fpu_data.csv'
fieldnames = ['date', 'time', 'wattage', 'x', 'y', 'z']
curr_uv = 0

def handle_fpu_data(client, userdata, message):
    global curr_uv
    payload = json.loads(message.payload.decode())
    print("handle_fpu_data:", payload)
    if payload['uv'] > curr_uv:
        curr_uv = payload['uv']
        print('increase x, decrease z')
    if payload['uv'] < curr_uv:
        curr_uv = payload['uv']
        print('increase z, decrease y')
    # with open(file_name, mode='a') as temperature_file:        
    #     temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
    #     temperature_writer.writerow({'date' : datetime.now().astimezone().replace(microsecond=0).isoformat(), 'temperature' : payload['temperature']})

mqtt_client.on_message = handle_fpu_data

# if not path.exists(file_name):
#     with open(file_name, mode='w') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()

while True:
    time.sleep(2)