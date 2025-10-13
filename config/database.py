# src/config/database.py
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

MYSQL_URI = os.getenv('MYSQL_URI')  # optional
SQLITE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data.db")
SQLITE_URI = f"sqlite:///{SQLITE_PATH}"

Base = declarative_base()

def get_engine():
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=False)
            conn = engine.connect()
            conn.close()
            logging.info("Connected to MySQL")
            return engine
        except OperationalError:
            logging.warning("Could not connect to MySQL. Falling back to SQLite.")
    return create_engine(SQLITE_URI, echo=False)

engine = get_engine()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def get_db_session():
    return SessionLocal()
