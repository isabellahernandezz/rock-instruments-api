from flask import Flask
from controllers.instrument_controller import instrument_bp  # Importa el Blueprint con todas las rutas de instrumentos

# Crear la aplicación Flask
app = Flask(__name__)

# Registrar el Blueprint para que todas las rutas definidas en instrument_bp estén disponibles
app.register_blueprint(instrument_bp)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta el servidor en modo debug
