# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y el código fuente
COPY requirements.txt ./
COPY src/ ./src

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto (ajusta si tu app usa otro)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "src/main.py"]
