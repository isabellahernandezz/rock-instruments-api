import os
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from src.models.db import db

# ========== Configuración ==========
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Swagger (documentación API)
app.config["SWAGGER"] = {"title": "FlaskAPIExample", "uiversion": 3}
Swagger(app)

# Base de datos
db_url = os.getenv("MYSQL_URL") or os.getenv("DATABASE_URL") or os.getenv("MYSQL_URI")
if db_url and db_url.startswith("mysql://"):
    db_url = db_url.replace("mysql://", "mysql+pymysql://", 1)
if not db_url:
    db_url = "sqlite:///app.db"
    logger.warning("No se definió MYSQL_URL. Usando SQLite local")

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "clave_jwt_por_defecto")

# Inicializar DB y JWT
db.init_app(app)
jwt = JWTManager(app)

# ========== Blueprints ==========
from src.controllers.user_controller import user_bp
from src.controllers.instrument_controller import instrument_bp

app.register_blueprint(user_bp)
app.register_blueprint(instrument_bp)

# ========== Rutas básicas ==========
@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/")
def index():
    return {
        "api": "FlaskAPIExample",
        "status": "OK",
        "description": "API REST modular con Flask, JWT y SQLAlchemy",
        "endpoints": {
            "POST /users/register": "Registro de usuario",
            "POST /users/login": "Login y JWT",
            "GET /users/": "Lista de usuarios (JWT)",
            "GET /api/instruments": "Lista de instrumentos (JWT)"
        }
    }, 200

# Crear tablas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 6060)), debug=True)
