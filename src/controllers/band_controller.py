from flask import Blueprint, request, jsonify
from src.app import db
from src.models.band_model import Band
from src.utils.decorators import role_required

band_bp = Blueprint('band_bp', __name__)

# ===============================
# Listar bandas (admin + user)
# ===============================
@band_bp.route('/', methods=['GET'])
@role_required('admin', 'user')
def list_bands():
    bands = Band.query.all()
    return jsonify([b.to_dict() for b in bands]), 200

# ===============================
# Crear banda (solo admin)
# ===============================
@band_bp.route('/', methods=['POST'])
@role_required('admin')
def create_band():
    data = request.get_json()
    name = data.get('name')
    genre = data.get('genre')
    origin = data.get('origin')

    if not name or not genre or not origin:
        return {'msg': 'Todos los campos son requeridos'}, 400

    new_band = Band(name=name, genre=genre, origin=origin)
    db.session.add(new_band)
    db.session.commit()

    return {'msg': 'Banda registrada exitosamente'}, 201

# ===============================
# Editar banda por id (solo admin)
# ===============================
@band_bp.route('/<int:id>', methods=['PUT'])
@role_required('admin')
def update_band(id):
    band = Band.query.get(id)
    if not band:
        return {'msg': 'Banda no encontrada'}, 404

    data = request.get_json()
    band.name = data.get('name', band.name)
    band.genre = data.get('genre', band.genre)
    band.origin = data.get('origin', band.origin)

    db.session.commit()
    return {'msg': 'Banda actualizada correctamente'}, 200

# ===============================
# Eliminar banda por id (solo admin)
# ===============================
@band_bp.route('/<int:id>', methods=['DELETE'])
@role_required('admin')
def delete_band(id):
    band = Band.query.get(id)
    if not band:
        return {'msg': 'Banda no encontrada'}, 404

    db.session.delete(band)
    db.session.commit()
    return {'msg': 'Banda eliminada correctamente'}, 200
