from paho.mqtt import client as mqtt_client
from random import randint
import time

broker = 'broker.hivemq.com'
port = 1883
topic = "esp/vagas"

# generate client ID with pub prefix randomly
client_id = 'ID'+str(randint(0,1000))
deviceId = 'D1'+str(randint(0,1000))

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print(rc)
        if rc==0:
            print("Conectado ao MQTT broker")
        else:
            print("Falha ao conectar, codigo de erro: %d", rc)
 
 
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
 
def publish(client):
    msg = '{"Vaga01":"Ocupada","Vaga02":"Livre","Vaga03":"Livre","Vaga04":"Ocupada"}'
    result = client.publish(topic,msg)
    msg_status = result[0]
    if msg_status ==0:
        print(f"Mensagem : {msg} enviada para o topico {topic}")
    else:
        print(f"Falha ao enviar a mensagem para o topico {topic}")
 

def main():
    client = connect_mqtt()
    while(1):
        publish(client)
        time.sleep(2)
    

if __name__ == '__main__':
    main()