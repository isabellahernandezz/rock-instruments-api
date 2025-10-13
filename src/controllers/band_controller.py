from flask import Blueprint, request, jsonify
from src.app import db
from src.models.band_model import Band
from flask_jwt_extended import jwt_required

band_bp = Blueprint('band_bp', __name__)

# Listar todas las bandas
@band_bp.route('/', methods=['GET'])
def get_bands():
    bands = Band.query.all()
    result = []
    for band in bands:
        result.append({
            "id": band.id,
            "name": band.name,
            "genre": band.genre,
            "country": band.country
        })
    return jsonify(result), 200

# Crear nueva banda
@band_bp.route('/', methods=['POST'])
@jwt_required()
def create_band():
    data = request.get_json()
    name = data.get('name')
    genre = data.get('genre')
    country = data.get('country')

    if not name or not genre or not country:
        return jsonify({"msg": "Todos los campos son requeridos"}), 400

    new_band = Band(name=name, genre=genre, country=country)
    db.session.add(new_band)
    db.session.commit()

    return jsonify({"msg": "Banda creada exitosamente"}), 201

# Actualizar banda
@band_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_band(id):
    band = Band.query.get_or_404(id)
    data = request.get_json()

    band.name = data.get('name', band.name)
    band.genre = data.get('genre', band.genre)
    band.country = data.get('country', band.country)

    db.session.commit()
    return jsonify({"msg": "Banda actualizada"}), 200

# Eliminar banda
@band_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_band(id):
    band = Band.query.get_or_404(id)
    db.session.delete(band)
    db.session.commit()
    return jsonify({"msg": "Banda eliminada"}), 200
