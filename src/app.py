import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bands.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')

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

    @app.route('/')
    def home():
        return {
            "message": "🎸 Bienvenido a la API de Rock Bands 🤘",
            "status": "running"
        }

    # Crear todas las tablas si no existen
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
