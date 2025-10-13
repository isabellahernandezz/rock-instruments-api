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

    # Blueprints con import relativo
    from .controllers.auth_controller import auth_bp
    from .controllers.band_controller import band_bp
    from .controllers.instrument_controller import instrument_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(band_bp, url_prefix="/bands")
    app.register_blueprint(instrument_bp, url_prefix="/instruments")

    @app.route('/')
    def home():
        return {
            "message": "🎸 Bienvenido a la API de Rock Bands 🤘",
            "status": "running"
        }

    with app.app_context():
        db.create_all()

    return app
