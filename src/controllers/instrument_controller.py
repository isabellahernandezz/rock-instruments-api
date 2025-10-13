from flask import Blueprint, request, jsonify
from src.app import db
from src.models.instrument_model import Instrument
from flask_jwt_extended import jwt_required

instrument_bp = Blueprint('instrument_bp', __name__)

# Listar instrumentos
@instrument_bp.route('/', methods=['GET'])
def get_instruments():
    instruments = Instrument.query.all()
    result = []
    for inst in instruments:
        result.append({
            "id": inst.id,
            "name": inst.name,
            "type": inst.type,
            "brand": inst.brand
        })
    return jsonify(result), 200

# Crear instrumento
@instrument_bp.route('/', methods=['POST'])
@jwt_required()
def create_instrument():
    data = request.get_json()
    name = data.get('name')
    type_ = data.get('type')
    brand = data.get('brand')

    if not name or not type_ or not brand:
        return jsonify({"msg": "Todos los campos son requeridos"}), 400

    new_inst = Instrument(name=name, type=type_, brand=brand)
    db.session.add(new_inst)
    db.session.commit()
    return jsonify({"msg": "Instrumento registrado exitosamente"}), 201

# Actualizar instrumento
@instrument_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_instrument(id):
    inst = Instrument.query.get_or_404(id)
    data = request.get_json()

    inst.name = data.get('name', inst.name)
    inst.type = data.get('type', inst.type)
    inst.brand = data.get('brand', inst.brand)

    db.session.commit()
    return jsonify({"msg": "Instrumento actualizado"}), 200

# Eliminar instrumento
@instrument_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_instrument(id):
    inst = Instrument.query.get_or_404(id)
    db.session.delete(inst)
    db.session.commit()
    return jsonify({"msg": "Instrumento eliminado"}), 200
