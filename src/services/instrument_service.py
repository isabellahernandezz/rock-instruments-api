from repositories.instrument_repository import InstrumentRepository
from sqlalchemy.orm import Session

# Servicio que actúa como capa intermedia entre las rutas (Flask) y el repositorio
# Aquí se podría agregar lógica de negocio adicional si fuera necesario
class InstrumentService:
    def __init__(self, db_session: Session):
        # Inicializa el repositorio con la sesión de la base de datos
        self.repository = InstrumentRepository(db_session)

    # Devuelve todos los instrumentos
    def listar_instruments(self):
        return self.repository.get_all_instruments()

    # Obtiene un instrumento por su ID
    def obtener_instrument(self, instrument_id: int):
        return self.repository.get_instrument_by_id(instrument_id)

    # Crea un nuevo instrumento
    def crear_instrument(self, name: str, type_: str):
        return self.repository.create_instrument(name, type_)

    # Actualiza un instrumento existente
    def actualizar_instrument(self, instrument_id: int, name: str = None, type_: str = None):
        return self.repository.update_instrument(instrument_id, name, type_)

    # Elimina un instrumento por su ID
    def eliminar_instrument(self, instrument_id: int):
        return self.repository.delete_instrument(instrument_id)
