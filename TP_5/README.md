# TP 5 - Comunicaciones de Datos

## Requisitos

- Python 3.8+
- pip

## Instalación

1. **Crear virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activar virtual environment:**

   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   - Crear archivo `.env` con las credenciales necesarias (ver `.env.example`)

## Ejecución

```bash
python main.py
```

## Variables de Entorno (.env)

- `USUARIO_HIVE` - Usuario HiveMQ
- `CONTRASENA_HIVE` - Contraseña HiveMQ
- `HOST_HIVE` - Host HiveMQ
