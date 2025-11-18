import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

USER_HIVE = os.getenv("USUARIO_HIVE")
PASSWORD_HIVE = os.getenv("CONTRASENA_HIVE")
HOST_HIVE = os.getenv("HOST_HIVE")

HOST = HOST_HIVE
USERNAME = USER_HIVE
PASSWORD = PASSWORD_HIVE



def on_connect(client, userdata, flags, rc):
    print("[SUB2] Conectado con código:", rc)
    client.subscribe("lan/broadcast/#")
    print("[SUB2] Suscrito a lan/broadcast/#")

def on_message(client, userdata, msg):
    print(f"[SUB2] Mensaje recibido: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client(client_id="sub_2")
client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

client.tls_set()  # HiveMQ Cloud exige TLS

client.connect(HOST, 8883)  # TLS port
client.loop_forever()
