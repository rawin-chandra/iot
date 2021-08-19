# python3.6

import mysql.connector
import random
from paho.mqtt import client as mqtt_client
from datetime import datetime

broker = '192.168.1.108'   #your mqtt beoker's I.P.
port = 1883
topic = "sensor/temp"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abcdefghijk",
  database="sensors"
)

print("mydb " , mydb)

mycursor = mydb.cursor()

print("my cursor " , mycursor)

insert = False

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


def subscribe(client: mqtt_client):
    #global insert,mydb,mycursor
    def on_message(client, userdata, msg):
        global insert   #,mydb,mycursor
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abcdefghijk",
        database="sensors"
        )

        print("mydb " , mydb)

        mycursor = mydb.cursor()


        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        temp = float(msg.payload.decode())

        temp = str(temp)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        min = int(now.strftime("%M"))

        #if min % 5 == 0:
        if True:
            if insert == False:
                sql = "INSERT INTO temp_sensor (date, time,temp) VALUES ('17/7/2564','" + current_time + "'," + temp + ")"
                mycursor.execute(sql)

                mydb.commit()

                print("insert data to temp_sensor database")
                insert = True
        else:
            insert = False

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
