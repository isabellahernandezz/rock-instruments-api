from flask import Blueprint, request, jsonify
from app import db
from models.instrument_model import Instrument

instrument_bp = Blueprint('instrument', __name__)

@instrument_bp.route('/', methods=['GET'])
def get_instruments():
    instruments = Instrument.query.all()
    result = [{'id': i.id, 'name': i.name, 'type': i.type} for i in instruments]
    return jsonify(result), 200

@instrument_bp.route('/', methods=['POST'])
def create_instrument():
    data = request.get_json()
    name = data.get('name')
    type_ = data.get('type', '')

    if not name:
        return jsonify({'msg': 'El nombre es requerido'}), 400

    new_instrument = Instrument(name=name, type=type_)
    db.session.add(new_instrument)
    db.session.commit()
    return jsonify({'msg': 'Instrumento creado', 'id': new_instrument.id}), 201
