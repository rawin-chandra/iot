# python3.6

import random
from paho.mqtt import client as mqtt_client
import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["temp_sensor"]

broker = '192.168.1.107'   #your mqtt beoker's I.P.
port = 1883
topic = "sensor/temp"
client_id = f'python-mqtt-{random.randint(0, 100)}'
min = 0

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

insert = False

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global insert
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        temp = float(msg.payload.decode())

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        mydict = { "date": "28/7/2564", "time": current_time , "temp": temp }
        x = mycol.insert_one(mydict)
        print("insert ",x , " to temp_sensor database")
        insert = True

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
