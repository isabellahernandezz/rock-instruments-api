import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Inicializar extensiones
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    # Cargar variables de entorno
    load_dotenv()

    app = Flask(__name__)

    # Configuración
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bands.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
    app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
    app.config['DEBUG'] = app.config['ENV'] == 'development'

    # Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)

    # Importar blueprints
    from src.controllers.auth_controller import auth_bp
    from src.controllers.band_controller import band_bp
    from src.controllers.instrument_controller import instrument_bp

    # Registrar blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(band_bp, url_prefix="/bands")
    app.register_blueprint(instrument_bp, url_prefix="/instruments")

    # Ruta de prueba
    @app.route('/')
    def home():
        return jsonify({
            "message": "🎸 Bienvenido a la API de Rock Bands 🤘",
            "status": "running"
        })

    # Crear todas las tablas si no existen
    with app.app_context():
        try:
            db.create_all()
            print("✅ Tablas creadas correctamente")
        except Exception as e:
            print(f"❌ Error creando tablas: {e}")

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
