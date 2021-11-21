import json
import time
import paho.mqtt.client as mqtt
from os import path
import csv
from datetime import datetime

id = 'csci_ecu_21_ant'
name = id + 'analytics_engine'
topic = id + '/data'
mqtt_client = mqtt.Client(name)
mqtt_client.connect('35.243.224.151')
mqtt_client.subscribe(topic)
mqtt_client.loop_start()

file_name = 'fpu_data.csv'
fieldnames = ['date', 'time', 'wattage', 'x', 'y', 'z']

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    # with open(file_name, mode='a') as temperature_file:        
    #     temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
    #     temperature_writer.writerow({'date' : datetime.now().astimezone().replace(microsecond=0).isoformat(), 'temperature' : payload['temperature']})

mqtt_client.on_message = handle_telemetry

# if not path.exists(file_name):
#     with open(file_name, mode='w') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()

while True:
    time.sleep(2)