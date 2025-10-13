from flask import Blueprint, request, jsonify
from src.app import db
from src.models.instrument_model import Instrument
from src.utils.decorators import role_required

instrument_bp = Blueprint('instrument_bp', __name__)

# ===============================
# Listar instrumentos (admin + user)
# ===============================
@instrument_bp.route('/', methods=['GET'])
@role_required('admin', 'user')
def list_instruments():
    instruments = Instrument.query.all()
    return jsonify([i.to_dict() for i in instruments]), 200

# ===============================
# Crear instrumento (solo admin)
# ===============================
@instrument_bp.route('/', methods=['POST'])
@role_required('admin')
def create_instrument():
    data = request.get_json()
    name = data.get('name')
    type_ = data.get('type')
    brand = data.get('brand')

    if not name or not type_ or not brand:
        return {'msg': 'Todos los campos son requeridos'}, 400

    new_instrument = Instrument(name=name, type=type_, brand=brand)
    db.session.add(new_instrument)
    db.session.commit()

    return {'msg': 'Instrumento registrado exitosamente'}, 201

# ===============================
# Editar instrumento por id (solo admin)
# ===============================
@instrument_bp.route('/<int:id>', methods=['PUT'])
@role_required('admin')
def update_instrument(id):
    instrument = Instrument.query.get(id)
    if not instrument:
        return {'msg': 'Instrumento no encontrado'}, 404

    data = request.get_json()
    instrument.name = data.get('name', instrument.name)
    instrument.type = data.get('type', instrument.type)
    instrument.brand = data.get('brand', instrument.brand)

    db.session.commit()
    return {'msg': 'Instrumento actualizado correctamente'}, 200

# ===============================
# Eliminar instrumento por id (solo admin)
# ===============================
@instrument_bp.route('/<int:id>', methods=['DELETE'])
@role_required('admin')
def delete_instrument(id):
    instrument = Instrument.query.get(id)
    if not instrument:
        return {'msg': 'Instrumento no encontrado'}, 404

    db.session.delete(instrument)
    db.session.commit()
    return {'msg': 'Instrumento eliminado correctamente'}, 200
