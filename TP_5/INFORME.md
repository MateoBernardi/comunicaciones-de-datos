# Universidad Nacional de Córdoba

## Facultad de Ciencias Exactas, Físicas y Naturales

### Ingeniería en Computación

---

# Informe - Comunicaciones de Datos

**Materia:** Comunicaciones de Datos  
**Trabajo Práctico N°:** 4

**Alumnos:** Mateo Bernardi - Santiago Madrid  
**Año:** 2025  
**Profesor:** Ing. Facundo Oliva Cuneo - Ing. Santiago Henn
**Fecha de entrega:** 25/08/2025

---

## Actividad 1

### Características del protocolo MQTT + Pub/Sub

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajeria liviano y eficiente. Permite su implementacion en microcontroladores pequeños, por los pocos recursos requeridos, y en redes con baja disponibilidad o alta latencia.
Su arquitectura se basa en comunicacion cliente-broker, y usa un patron publish/subscribe.

#### Características principales:
- Liviano: headers pequeños, ideal para IoT.
- Funciona sobre TCP.
- Implementa un patron publish/subscribe mediante un broker.
- QoS configurables entre 3 diferentes niveles: 0 (como mucho una vez), 1 (al menos una vez) y 2 (exactamente una vez).
- Topicos jerarquicos con uso de wildcards como "*" o "#".

#### Desventajas
- Dependencia total del broker.
- No tiene cifrado propio, necesita TLS.
- No es optimo para archivos grandes.
- No es optimo cuando se requieren latencias ultra bajas.
- Necesita redes con cierta estabilidad.

#### Usos principales
- Robotica en procesos de manufactura.
- IoT, tanto domótica como industrial.
- Automatización y monitoreo remoto.
- Sistemas distribuidos simples.

## Actividad 2
### Instalacion y despliegue de un broker MQTT

Para implementar el broker MQTT, se utilizó el servicio HiveMQ Cloud. El proceso consistió en:

1. **Registro en HiveMQ Cloud:** Se creó una cuenta en la plataforma para acceder a los servicios de broker en la nube.
2. **Creación de un cluster:** Se generó un nuevo cluster MQTT, lo que permite disponer de un broker dedicado y seguro en la nube.
3. **Configuración del cluster:** Se obtuvieron las credenciales de acceso (host, puerto, usuario y contraseña) necesarias para conectar clientes MQTT al broker.
4. **Gestión de usuarios:** Se configuraron los usuarios y permisos para controlar el acceso de los clientes al broker.
5. **Verificación de la conexión:** Se probaron las credenciales y la conectividad utilizando clientes MQTT (publisher y subscribers) desarrollados en Python, asegurando la comunicación exitosa entre los dispositivos y el broker.
6. **Monitoreo:** Se utilizó el panel de HiveMQ Cloud para visualizar la actividad del cluster, los mensajes transmitidos y los clientes conectados.

Este proceso permitió desplegar un entorno MQTT funcional y seguro, facilitando la comunicación entre dispositivos mediante el patrón publish/subscribe. 
![alt text](images/image.png)
Conexión via web client:
![alt text](image-2.png)

## Actividad 3 y 4
### Conexión entre diferentes clientes

Se intento una conexion desde diferentes clientes

Cliente que envia el mensaje:
![alt text](image-1.png)

Cliente subscriptor del mensaje:
![alt text](image-3.png)

![alt text](image-4.png)

En otra prueba, se quieso establecer conexión broadcast donde el cliente web envia un mensaje a todos los clientes suscritos a `lan/broadcast/#`:
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)

Tambien se probo un script en python estableciendo un cliente para recibir los mensajes del broadcast.

![alt text](image-8.png)

## Actividad 5
### Simulacion de una red usando MQTT

En primera instancia se generaron 3 clientes que envian informacion de sensores de diferentes ambientes
![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)

Luego un gateway que recibe todos los mensajes de la sala, y tambien los comandos desde el controlador, que le avisa a los sensores cuando enviar o dejar de enviar datos (comandos start y stop)
![alt text](image-12.png)

Desde el cliente web se puede ver los mensajes recibidos suscribiendose a `lan/#`

![alt text](image-13.png)

En esta terminal se puede ver la simulacion antes de enviar el comando `start`, y luego en ejecucion cuando se envia el comando `stop`.

![alt text](image-14.png)
![alt text](image-15.png)
![alt text](image-16.png)

Por ultimo usando `matplotlib` pudimos graficar los datos de temperatura recibidos en el gateway, registrados en un .csv
![alt text](image-17.png)
![alt text](image-18.png)
![alt text](image-19.png)

Para ver el trafico de datos, utilizamos WireShark para interceptar paquetes y revisar su contenido.
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)

#### Teórico actividad 5:

a) ¿Sobre qué protocolos de capa de transporte están trabajando?

Principalmente:
TCP (el más común en MQTT).
Proporciona conexión confiable, ordenada y sin pérdidas.
UDP no se usa en MQTT estándar, pero sí en variantes como MQTT-SN.
En tu práctica, solo trabajaron sobre TCP (lo podés verificar en Wireshark: MQTT / TCP / IP).

b) Integridad, Confidencialidad y Disponibilidad en esta arquitectura

Integridad:
MQTT no tiene integridad propia salvo controles mínimos.
Se apoya totalmente en TCP, que garantiza orden y detección de pérdidas.
Si no se usa TLS, un atacante puede modificar paquetes.
Integridad razonable si se usa TCP, débil sin mecanismo criptográfico.

Confidencialidad:
No existe por defecto.
Todo viaja en texto claro si no se usa TLS.
Cualquiera en la LAN puede leer mensajes con Wireshark.
Confidencialidad solo está garantizada si se usa MQTT sobre TLS (MQTTS).

Disponibilidad:
Depende críticamente del broker. Si cae, la red se detiene.
MQTT está diseñado para IoT de bajo consumo, pero no es tolerante a fallas severas.
Buena disponibilidad si el broker está bien configurado, pero un único punto de falla.

c) Rol de los niveles de QoS en la fiabilidad

El QoS determina cuánta garantía de entrega tiene un mensaje:
QoS 0: Puede perderse → fiabilidad mínima.
QoS 1: Se entrega al menos una vez → buena fiabilidad pero puede haber duplicados.
QoS 2: Se entrega exactamente una vez → máxima fiabilidad, más lento.

QoS te permite equilibrar consumo / velocidad / fiabilidad según el tipo de dato.
En sensores de tu TP, QoS 0 o 1 es típico.

d) Ventajas del modelo pub/sub vs cliente-servidor

Pub/Sub (MQTT):
Los emisores (publishers) y los receptores (subscribers) nunca se conocen entre sí.
El broker desacopla completamente.

Permite:
Escalabilidad masiva.
Sensores livianos.
Múltiples consumidores para un mismo dato.
Menor tráfico (solo se envía lo que alguien pidió).

Cliente-servidor:
El cliente debe conectarse directamente al servidor.
No escala bien si hay muchos clientes.
Pub/Sub es ideal para IoT y redes con muchos sensores porque desacopla, escala mejor y reduce carga.

e) Limitaciones de MQTT en una red LAN real

Fiabilidad limitada si no se usa QoS 1 o 2.
Sin seguridad por defecto (ni autenticación fuerte, ni cifrado).
Depende de un broker: si se cae, muere la comunicación.
No maneja grandes volúmenes de datos (pensado para mensajes cortos).
Latencia mayor vs un protocolo directo sobre UDP.
No está pensado para throughput alto, sino para mensajes pequeños.
En una LAN de alto rendimiento, MQTT queda corto comparado con protocolos como ZeroMQ, gRPC o WebSockets puros.

f) Implicaciones de depender de un broker central

Desventaja principal: es un single point of failure.

- Si el broker falla, se congestiona, pierde conexión.

- También implica mayor latencia (todo pasa por el broker).

- Dependencia de la configuración del broker para seguridad y autenticación.

- Riesgo de cuello de botella si hay muchos sensores.

Ventaja:
Centraliza control, logging, autenticación, retención de mensajes, ACLs y administración.

Para una chica es excelente, pero en sistemas críticos se recomienda HA (alta disponibilidad) o brokers redundantes.
