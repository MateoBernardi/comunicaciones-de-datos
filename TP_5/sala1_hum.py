import paho.mqtt.client as mqtt
import time, random
from dotenv import load_dotenv
import os

load_dotenv()

BROKER = os.getenv("HOST_HIVE")
PORT = 8883
USER = os.getenv("USUARIO_HIVE")
PASSWORD = os.getenv("CONTRASENA_HIVE")

running = False   # <<< ARRANCA DETENIDO

def on_message(client, userdata, msg):
    global running
    comando = msg.payload.decode()

    if msg.topic == "lan/cmd/start":
        print(">> START recibido")
        running = True

    elif msg.topic == "lan/cmd/stop":
        print(">> STOP recibido")
        running = False


client = mqtt.Client()
client.username_pw_set(USER, PASSWORD)
client.tls_set()

client.on_message = on_message

client.connect(BROKER, PORT)

client.subscribe("lan/cmd/#")

# <<< MUY IMPORTANTE
client.loop_start()

while True:
    if running:
        valor = round(random.uniform(40, 70), 2)
        client.publish("lan/sala1/sensor/hum", valor)
        print("sala1 hum →", valor)

    time.sleep(2)

