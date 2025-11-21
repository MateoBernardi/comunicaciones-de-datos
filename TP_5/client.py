import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

USER_HIVE = os.getenv("USUARIO_HIVE")
PASSWORD_HIVE = os.getenv("CONTRASENA_HIVE")
HOST_HIVE = os.getenv("HOST_HIVE")

topic = "test/topic"

def on_connect(client, userdata, flags, rc, properties=None):
    print("Conectado con código:", rc)
    client.subscribe(topic)
    client.publish(topic, "¡Hola! KanyeWeb está conectado al broadcast.")
    
def on_message(client, userdata, msg):
    print("Mensaje recibido:", msg.topic, msg.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.username_pw_set(USER_HIVE, PASSWORD_HIVE)

client.tls_set()  # HiveMQ Cloud exige TLS

client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST_HIVE, 8883)
client.loop_forever()
