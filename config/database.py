import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from models.instrument_model import Base
from dotenv import load_dotenv

# Configura logging y carga variables del archivo .env
logging.basicConfig(level=logging.INFO)
load_dotenv()

# URI de la base de datos MySQL desde .env y URI de respaldo SQLite
MYSQL_URI = os.getenv('MYSQL_URI')
SQLITE_URI = 'sqlite:///instruments_local.db'

# Función que retorna un engine de SQLAlchemy
# Intenta usar MySQL si está disponible, si falla usa SQLite local
def get_engine():
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            conn = engine.connect()
            conn.close()
            logging.info('Conexión a MySQL exitosa.')
            return engine
        except OperationalError:
            logging.warning('No se pudo conectar a MySQL. Usando SQLite local.')
    engine = create_engine(SQLITE_URI, echo=True)
    return engine

# Creamos engine y sesión para interactuar con la base de datos
engine = get_engine()
Session = sessionmaker(bind=engine)

# Crea las tablas definidas en Base si no existen
Base.metadata.create_all(engine)

# Función para obtener una sesión de base de datos lista para usar
def get_db_session():
    return Session()
