import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Configura logging y carga variables del archivo .env
logging.basicConfig(level=logging.INFO)
load_dotenv()

# URI de la base de datos MySQL desde .env y URI de respaldo SQLite
MYSQL_URI = os.getenv('MYSQL_URI')
SQLITE_URI = 'sqlite:///instruments_local.db'

# Base para los modelos
Base = declarative_base()

# Función que retorna un engine de SQLAlchemy
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
    return create_engine(SQLITE_URI, echo=True)

# Creamos engine y sesión
engine = get_engine()
SessionLocal = sessionmaker(bind=engine)

# Función para obtener una sesión de base de datos
def get_db_session():
    return SessionLocal()
