from flask import Blueprint, request, jsonify
from src.app import db
from src.models.user_model import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')  # Por defecto 'user'

    if not email or not password:
        return jsonify({'msg': 'Email y contraseña son requeridos'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'El email ya está registrado'}), 400

    new_user = User(email=email, role=role)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'msg': f'Usuario {email} registrado exitosamente'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'msg': 'Credenciales inválidas'}), 401

    access_token = create_access_token(identity=email, expires_delta=timedelta(hours=2))
    return jsonify({
        'access_token': access_token,
        'role': user.role
    }), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    email = get_jwt_identity()
    user = User.query.filter_by(email=email).first()
    return jsonify({
        'email': user.email,
        'role': user.role
    }), 200
