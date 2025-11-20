import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

BROKER = os.getenv("HOST_HIVE")
PORT = 8883
USER = os.getenv("USUARIO_HIVE")
PASSWORD = os.getenv("CONTRASENA_HIVE")

client = mqtt.Client()
client.username_pw_set(USER, PASSWORD)
client.tls_set()
client.connect(BROKER, PORT)

cmd = input("Comando (start/stop): ")

if cmd == "start":
    client.publish("lan/cmd/start", "go")
    print(">> Enviado START")
elif cmd == "stop":
    client.publish("lan/cmd/stop", "halt")
    print(">> Enviado STOP")
else:
    print("Comando inválido")
