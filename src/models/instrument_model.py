from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Creamos la base de declarativos de SQLAlchemy
Base = declarative_base()

# Modelo que representa la tabla 'instruments' en la base de datos
class Instrument(Base):
    __tablename__ = 'instruments'  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # ID único
    name = Column(String(255), nullable=False)         # Nombre del instrumento (obligatorio)
    type = Column(String(100), nullable=False)         # Tipo del instrumento (obligatorio)
