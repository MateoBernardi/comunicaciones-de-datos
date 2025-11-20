import csv
from datetime import datetime
import matplotlib.pyplot as plt

ARCHIVO = "sensores.csv"
TOPIC_FILTRADO = "lan/sala2/sensor/temp"   # <-- cambiá este para plotear otro sensor

timestamps = []
valores = []

with open(ARCHIVO, "r") as f:
    reader = csv.reader(f)
    next(reader)  # saltea encabezado

    for ts, topic, valor in reader:
        if topic != TOPIC_FILTRADO:
            continue
        
        timestamps.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"))
        valores.append(float(valor))

# Tomar solo los últimos 10
timestamps = timestamps[-10:]
valores = valores[-10:]

plt.figure(figsize=(8,4))
plt.plot(timestamps, valores, marker="o")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.title(f"Últimos 10 valores - {TOPIC_FILTRADO}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
