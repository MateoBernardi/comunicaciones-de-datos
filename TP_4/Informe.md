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

1. Según el alcance las redes se pueden clasificar en:
    - Red de área personal (PAN), hablamos de una red de pocos metros, sirven para conectar dispositivos personales. Bajo consumo de energía.
    - Red de área local (LAN), es la que suele instalarse en la mayoría de las empresas. Alta velocidad, generalmente cableada o Wi-Fi.
    - Red de área de campus (CAN), varias redes de área local instaladas en áreas específicas, pero a su vez todas ellas interconectadas,
    - Red de área metropolitana (MAN), abarcan espacios metropolitanos mucho más grandes. Usualmente operadores de telecomunicaciones la gestionan.
    - Red de área amplia (WAN), Conecta múltiples LAN y MAN a gran distancia. Uso de líneas dedicadas, satélite o internet.
    - Red de área de almacenamiento (SAN), Conecta servidores y sistemas de almacenamiento de datos. Optimizada para transferencia masiva y alta disponibilidad.

2. Una VLAN es una red lógica creada dentro de un mismo switch físico para segmentar el tráfico, divide los grupos de usuarios de la red de una red física real en segmentos de redes lógicas. Es posible configurar varios dispositivos lógicos VLAN en un solo sistema. Cada dispositivo lógico VLAN constituye una instancia adicional del adaptador Ethernet. Estos dispositivos lógicos pueden utilizarse para configurar las mismas interfaces IP de Ethernet que se utilizan con los adaptadores Ethernet físicos.
Se pueden clasificar en:
    - VLAN por puerto, cada puerto se asigna manualmente a una VLAN. Es la más común y simple.
    - VLAN dinámica, el switch asigna automáticamente un puerto a una VLAN según la MAC detectada, usando un servidor VMPS.
    - VLAN por protocolo, agrupa tráfico según protocolo, útil en entornos mixtos antiguos.
    - VLAN por dirección IP o subred, agrupa dispositivos dentro de una misma subred IP, aunque estén en distintos switches.
    - VLAN por usuario, el usuario pertenece a una VLAN sin importar dónde se conecte, usando autenticación.
    - VLAN nativa, es la VLAN no etiquetada (por defecto VLAN 1) que se usa para tráfico no marcado en enlaces troncales.

3. Es un estándar desarrollado por el grupo de trabajo 802 de la IEEE para permitir que múltiples redes compartan de forma transparente el mismo medio físico sin interferencias, mediante el mecanismo de trunking.
Este estándar define el protocolo de etiquetado de tramas en redes Ethernet, lo que permite el transporte de tráfico de múltiples VLAN a través de un solo enlace troncal.

4. Es el proceso de añadir una etiqueta o marca especial dentro del frame Ethernet para indicar a qué VLAN pertenece ese tráfico. Se usa entre switches, entre switch y router, siempre que se transporten múltiples VLAN por el mismo enlace físico. 
Permite a los switches distinguir a qué VLAN pertenece cada trama cuando viajan por un mismo enlace físico.

## Actividad 2

En esta actividad se implementa la siguiente topología en Packet Tracer
<img width="1128" height="297" alt="image" src="https://github.com/user-attachments/assets/bd7c2241-cb9f-4c09-be8d-b35a332128ac" />

<img width="1601" height="413" alt="image" src="https://github.com/user-attachments/assets/f61d3df6-7be3-4ecf-928f-3d41be8d714e" />

<img width="1327" height="545" alt="image" src="https://github.com/user-attachments/assets/7b3e3975-785b-484d-8012-f7955574a9d3" />

a) Nombrar los switch como sw1 y sw2.
- Se puso como contraseña de la consola: `contrasena_consola`.
- Se puso como contraseña de exec: `contrasena_exec`.
- Se utilizo `service password-encryption` para encriptar las contraseñas.

d) Se configuraron las VLAN segun la tabla de direcciones

<img width="1063" height="320" alt="image" src="https://github.com/user-attachments/assets/03885a7d-0169-4b7f-aa56-325c443c107a" />

e) Se desconectaron todas las interfaces que no estaban siendo utilizadas.

<img width="672" height="589" alt="image" src="https://github.com/user-attachments/assets/c984940c-9218-45a4-b154-957ab8ac0503" />

g) En este punto se testeó la comunicación haciendo ping entre computadoras.

<img width="526" height="702" alt="image" src="https://github.com/user-attachments/assets/af420879-ea55-4085-98fd-d480c245544a" />

<img width="548" height="698" alt="image" src="https://github.com/user-attachments/assets/76bc5a72-b7a1-4367-9bed-7dd77984d3db" />

h) Se crearon VLAN en ambos switches.

<img width="472" height="182" alt="image" src="https://github.com/user-attachments/assets/3de26951-1979-4fc9-a856-d1ab5fd1e652" />
<img width="549" height="138" alt="image" src="https://github.com/user-attachments/assets/9d0b69dd-a9e6-4175-acb7-bf63a79bcd44" />

i) Visualizamos la lista de VLANs.

<img width="394" height="307" alt="image" src="https://github.com/user-attachments/assets/aa4017e1-47ac-4445-89cf-c1ef95820083" />
Por defecto se utiliza la VLAN `vlan 1`.

l) Se cambio el puerto a la VLAN Laboratorio. Verificar estado de la VLAN.

<img width="547" height="462" alt="image" src="https://github.com/user-attachments/assets/613309f9-07bc-44b6-a616-aa26b9ce3552" />

- VLAN 10 Lab: Tiene asignado el puerto Fa0/6

<img width="672" height="587" alt="image" src="https://github.com/user-attachments/assets/0475d7c9-1086-46a0-a073-74b541dbcb96" />

n) Verificar conexion entre PC-A y PC-B usando pings.

<img width="704" height="462" alt="image" src="https://github.com/user-attachments/assets/5e94da2b-cf02-4db3-b380-e144dc7da9e4" />
<img width="746" height="455" alt="image" src="https://github.com/user-attachments/assets/a255ad2f-6087-4ff0-b08d-ea28d109d7e6" />

Conectividad entre pcs:
Las dos PCs pertenecen a la VLAN Laboratorio configurada en los switches.
Las PCs en la VLAN 10 se comunican correctamente entre sí a través de los dos switches. Se  confirma el correcto funcionamiento de la segmentación por VLAN y la conectividad de capa 2.

## Actividad 3

Utilizando lo que aprendimos sobre VLAN, e investigando la configuración de NAT y ACLs,
simularemos el despliegue de una red LAN a bordo de una aeronave. La idea es la siguiente, tendremos
tres segmentos:
i) Clase Turista: acceso solo a un sistema de entretenimiento (server local)
ii) Clase Business: acceso a sistema de entretenimiento e internet.
iii) Administración: acceso total.

<img width="1343" height="460" alt="image" src="https://github.com/user-attachments/assets/4a1c77fd-9839-4030-9bfd-8d2c3b559d95" />

Topología:
<img width="683" height="590" alt="image" src="https://github.com/user-attachments/assets/56dc63b2-237e-4e2f-acbf-776ba0361f03" />

Y la siguiente tabla de direccionamiento:

<img width="863" height="220" alt="image" src="https://github.com/user-attachments/assets/53f6cf25-936d-434e-88f7-447639f6c323" />

--- 
<img width="879" height="756" alt="image" src="https://github.com/user-attachments/assets/af805c45-45c3-47e1-a559-a43c4aca1bc2" />

Pruebas

<img width="863" height="434" alt="image" src="https://github.com/user-attachments/assets/12976a83-8ef0-405a-8189-5ea9d34d7413" />

Ping al servidor de entretenimiento - De PC turista a 10.10.99.254

<img width="580" height="388" alt="image" src="https://github.com/user-attachments/assets/22299c6b-f829-4799-b21c-be0a27fefd39" />

Acceso HTTP al servidor local 

<img width="835" height="845" alt="image" src="https://github.com/user-attachments/assets/ce3ffeae-7aeb-4e9d-9c8b-ee473c0cb998" />

Ping a internet desde PC Turista

<img width="573" height="316" alt="image" src="https://github.com/user-attachments/assets/ac62714b-81b3-4988-8830-5f7e1e3fd65a" />

Acceso HTTP al servidor local - desde PC business

<img width="825" height="845" alt="image" src="https://github.com/user-attachments/assets/dc03eb38-bf42-4840-ba1c-83d3bc5b6d4a" />

Ping a internet desde PC Business

<img width="690" height="459" alt="image" src="https://github.com/user-attachments/assets/5f45257d-5f97-46e2-9646-ca354dbad31e" />

Ping entre admin y todos

<img width="869" height="710" alt="image" src="https://github.com/user-attachments/assets/26efe869-c887-4a4c-bda5-d34923ffd5ba" />
<img width="636" height="411" alt="image" src="https://github.com/user-attachments/assets/1fcf0430-47d1-4f18-82ea-b8b00f8a1c27" />
