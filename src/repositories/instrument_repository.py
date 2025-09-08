from models.instrument_model import Instrument
from sqlalchemy.orm import Session

class InstrumentRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_instruments(self):
        return self.db.query(Instrument).all()

    def get_instrument_by_id(self, instrument_id: int):
        return self.db.query(Instrument).filter(Instrument.id == instrument_id).first()

    def create_instrument(self, name: str, type_: str):
        inst = Instrument(name=name, type=type_)
        self.db.add(inst)
        self.db.commit()
        self.db.refresh(inst)
        return inst

    def update_instrument(self, instrument_id: int, name: str = None, type_: str = None):
        inst = self.get_instrument_by_id(instrument_id)
        if inst:
            if name: inst.name = name
            if type_: inst.type = type_
            self.db.commit()
            self.db.refresh(inst)
        return inst

    def delete_instrument(self, instrument_id: int):
        inst = self.get_instrument_by_id(instrument_id)
        if inst:
            self.db.delete(inst)
            self.db.commit()
        return inst
