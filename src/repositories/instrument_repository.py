from models.instrument_model import Instrument
from sqlalchemy.orm import Session

# Repositorio que maneja la interacción directa con la base de datos
# Encapsula todas las operaciones CRUD para los instrumentos
class InstrumentRepository:
    def __init__(self, db_session: Session):
        self.db = db_session  # Guarda la sesión de SQLAlchemy para usarla en todas las operaciones

    # Devuelve todos los instrumentos de la base de datos
    def get_all_instruments(self):
        return self.db.query(Instrument).all()

    # Devuelve un instrumento específico por su ID
    def get_instrument_by_id(self, instrument_id: int):
        return self.db.query(Instrument).filter(Instrument.id == instrument_id).first()

    # Crea un nuevo instrumento en la base de datos
    def create_instrument(self, name: str, type_: str):
        inst = Instrument(name=name, type=type_)
        self.db.add(inst)  # Agrega el instrumento a la sesión
        self.db.commit()   # Guarda los cambios en la base de datos
        self.db.refresh(inst)  # Refresca la instancia para obtener los valores actuales de la DB
        return inst

    # Actualiza un instrumento existente (nombre y/o tipo)
    def update_instrument(self, instrument_id: int, name: str = None, type_: str = None):
        inst = self.get_instrument_by_id(instrument_id)
        if inst:
            if name: inst.name = name
            if type_: inst.type = type_
            self.db.commit()    # Guarda los cambios
            self.db.refresh(inst)  # Refresca la instancia
        return inst

    # Elimina un instrumento de la base de datos
    def delete_instrument(self, instrument_id: int):
        inst = self.get_instrument_by_id(instrument_id)
        if inst:
            self.db.delete(inst)  # Marca el instrumento para eliminación
            self.db.commit()      # Aplica los cambios en la DB
        return inst
