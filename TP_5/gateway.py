import paho.mqtt.client as mqtt
import csv
import time
from dotenv import load_dotenv
import os

load_dotenv()

BROKER = os.getenv("HOST_HIVE")
PORT = 8883
USER = os.getenv("USUARIO_HIVE")
PASSWORD = os.getenv("CONTRASENA_HIVE")

csv_file = open("sensores.csv", "a", newline="")
writer = csv.writer(csv_file)
writer.writerow(["timestamp", "topic", "valor"])

def on_message(client, userdata, msg):
    valor = msg.payload.decode()
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[GATEWAY] {ts} | {msg.topic} → {valor}")
    writer.writerow([ts, msg.topic, valor])
    csv_file.flush()

client = mqtt.Client()
client.username_pw_set(USER, PASSWORD)
client.tls_set()
client.on_message = on_message

client.connect(BROKER, PORT)

client.subscribe("lan/+/sensor/+")
client.loop_forever()
