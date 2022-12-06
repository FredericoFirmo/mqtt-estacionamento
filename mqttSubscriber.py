import json
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic = "esp/vagas"


client_id = 'ID'+str(randint(0,1000))
deviceId = 'ID'+str(randint(0,1000))

class Subscriber():
    #@staticmethod
    def connect_mqtt():
        def on_connect(client, userdata, flags, rc):
            if rc==0:
                print("Conectado ao MQTT broker")
            else:
                print("Falha ao conectar, codigo de erro: %d", rc)
    
    
        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

    #@staticmethod
    def subscribe(client: mqtt_client,ui,MainWindow):
        def on_message(client, userdata,msg):
            print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
            msgfull=  msg.payload.decode()
            msgfull= msgfull.replace("'", '"')
            retorno = json.loads(msgfull)
            ui.updateUI(MainWindow,retorno)
        
        client.subscribe(topic)
        client.on_message = on_message