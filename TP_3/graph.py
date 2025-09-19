import matplotlib.pyplot as plt
import numpy as np

# Datos de las tecnologías (distancia en metros, data rate en bps)
technologies = {
    'Wi-Fi': (100, 1e9),
    'Bluetooth': (10, 2e6),
    'ZigBee': (100, 250e3),
    'NFC': (0.1, 424e3),
    'LTE': (10000, 100e6),
    'GSM': (35000, 270e3),
    '5G': (1000, 10e9),
    'LoRa': (15000, 50e3),
    'NB-IoT': (10000, 200e3),
    'SigFox': (50000, 100),
    'Z-Wave': (30, 100e3)
}

# Crear figura y ejes
plt.figure(figsize=(12, 8))

# Configurar escalas logarítmicas
plt.xscale('log')
plt.yscale('log')

# Plotear cada tecnología
colors = plt.cm.Set3(np.linspace(0, 1, len(technologies)))
for i, (tech, (distance, data_rate)) in enumerate(technologies.items()):
    plt.scatter(distance, data_rate, s=100, c=[colors[i]], 
               edgecolor='black', linewidth=1, alpha=0.8)
    
    # Agregar etiquetas con offset para evitar superposición
    offset_x = distance * 1.2 if distance < 1000 else distance * 0.8
    offset_y = data_rate * 1.1 if data_rate > 1e6 else data_rate * 0.9
    
    plt.annotate(tech, (distance, data_rate), 
                xytext=(offset_x, offset_y),
                fontsize=10, ha='left', va='bottom',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         alpha=0.7, edgecolor='gray'))

# Configurar ejes
plt.xlabel('Distance', fontsize=14, fontweight='bold')
plt.ylabel('Data rate [bps]', fontsize=14, fontweight='bold')

# Configurar límites y ticks
plt.xlim(0.1, 100000)
plt.ylim(1, 1.2e10)

# Configurar ticks personalizados
x_ticks = [1, 10, 100, 1000, 10000]
x_labels = ['1m', '10m', '100m', '1km', '10km']
plt.xticks(x_ticks, x_labels)

y_ticks = [1, 1e3, 1e6, 1e9]
y_labels = ['1', '10³', '10⁶', '10⁹']
plt.yticks(y_ticks, y_labels)

# Agregar grilla
plt.grid(True, alpha=0.3, linestyle='--')

# Agregar título
plt.title('Tecnologías Inalámbricas: Alcance vs Velocidad de Datos', 
          fontsize=16, fontweight='bold', pad=20)

# Ajustar layout
plt.tight_layout()

# Mostrar gráfico
plt.show()

# Función para agregar nueva tecnología
def add_technology(name, distance_m, data_rate_bps):
    """
    Agregar nueva tecnología al gráfico
    
    Args:
        name (str): Nombre de la tecnología
        distance_m (float): Alcance en metros
        data_rate_bps (float): Velocidad de datos en bps
    """
    technologies[name] = (distance_m, data_rate_bps)
    print(f"Tecnología '{name}' agregada: {distance_m}m, {data_rate_bps} bps")

# Función para modificar tecnología existente
def modify_technology(name, distance_m=None, data_rate_bps=None):
    """
    Modificar tecnología existente
    
    Args:
        name (str): Nombre de la tecnología
        distance_m (float, optional): Nuevo alcance en metros
        data_rate_bps (float, optional): Nueva velocidad de datos en bps
    """
    if name in technologies:
        current_distance, current_rate = technologies[name]
        new_distance = distance_m if distance_m is not None else current_distance
        new_rate = data_rate_bps if data_rate_bps is not None else current_rate
        technologies[name] = (new_distance, new_rate)
        print(f"Tecnología '{name}' modificada: {new_distance}m, {new_rate} bps")
    else:
        print(f"Tecnología '{name}' no encontrada")

# Ejemplos de uso:
# add_technology('6G', 500, 100e9)
# modify_technology('Wi-Fi', data_rate_bps=5e9)

print("Script cargado exitosamente!")
print("Tecnologías disponibles:")
for tech, (dist, rate) in technologies.items():
    print(f"  {tech}: {dist}m, {rate:.0e} bps")