from flask import Blueprint, request, jsonify
from app import db
from ..models.band_model import Band

band_bp = Blueprint('band', __name__)

@band_bp.route('/', methods=['GET'])
def get_bands():
    bands = Band.query.all()
    result = [{'id': b.id, 'name': b.name, 'genre': b.genre} for b in bands]
    return jsonify(result), 200

@band_bp.route('/', methods=['POST'])
def create_band():
    data = request.get_json()
    name = data.get('name')
    genre = data.get('genre', '')

    if not name:
        return jsonify({'msg': 'El nombre es requerido'}), 400

    new_band = Band(name=name, genre=genre)
    db.session.add(new_band)
    db.session.commit()
    return jsonify({'msg': 'Banda creada', 'id': new_band.id}), 201
