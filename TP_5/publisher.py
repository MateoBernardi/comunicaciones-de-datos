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

client = mqtt.Client(client_id="central_publisher")
client.username_pw_set(USERNAME, PASSWORD)

client.tls_set()  # HiveMQ Cloud exige TLS

client.connect(HOST, 8883)

topic = "lan/broadcast/all"
msg = "Mensaje de broadcast desde el cliente central"

print("[PUB] Publicando...")
client.publish(topic, msg)
print("[PUB] Mensaje enviado")

client.disconnect()
