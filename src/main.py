import os
from flask import Flask
from src.controllers.instrument_controller import instrument_bp
from src.config.database import Base, engine

app = Flask(__name__)
app.register_blueprint(instrument_bp)

# Crear tablas si no existen
with engine.begin() as conn:
    Base.metadata.create_all(bind=conn)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))  # Railway define PORT automáticamente
    app.run(host="0.0.0.0", port=port)
