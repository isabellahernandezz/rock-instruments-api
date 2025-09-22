from repositories.instrument_repository import InstrumentRepository
from sqlalchemy.orm import Session

class InstrumentService:
    def __init__(self, db_session: Session):
        self.repository = InstrumentRepository(db_session)

    def listar_instruments(self):
        return self.repository.get_all_instruments()

    def obtener_instrument(self, instrument_id: int):
        return self.repository.get_instrument_by_id(instrument_id)

    def crear_instrument(self, name: str, type_: str):
        return self.repository.create_instrument(name, type_)

    def actualizar_instrument(self, instrument_id: int, name: str = None, type_: str = None):
        return self.repository.update_instrument(instrument_id, name, type_)

    def eliminar_instrument(self, instrument_id: int):
        return self.repository.delete_instrument(instrument_id)
