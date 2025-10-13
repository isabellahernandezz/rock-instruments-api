from flask import Blueprint, request, jsonify
from src.app import db
from src.models.user_model import User
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    get_jwt_identity, get_jwt
)
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

# Lista negra de tokens (en memoria, para logout)
jwt_blacklist = set()

# --------- Registro de usuario ---------
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')

    if not email or not password:
        return jsonify({'msg': 'Email y contraseña son requeridos'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'El email ya está registrado'}), 400

    new_user = User(email=email, role=role)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'msg': 'Usuario registrado exitosamente'}), 201

# --------- Login ---------
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'msg': 'Credenciales inválidas'}), 401

    access_token = create_access_token(identity=email, expires_delta=timedelta(hours=2))
    refresh_token = create_refresh_token(identity=email)

    return jsonify({
        'access_token': access_token,
        'refresh_token': refresh_token,
        'role': user.role
    }), 200

# --------- Ver perfil ---------
@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    email = get_jwt_identity()
    user = User.query.filter_by(email=email).first()
    return jsonify({
        'email': user.email,
        'role': user.role
    }), 200

# --------- Refresh token ---------
@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    new_access = create_access_token(identity=identity, expires_delta=timedelta(hours=2))
    return jsonify({'access_token': new_access}), 200

# --------- Logout ---------
@auth_bp.route('/logout', methods=['POST'])
@jwt_required(refresh=True)
def logout():
    jti = get_jwt()['jti']
    jwt_blacklist.add(jti)
    return jsonify({"msg": "Refresh token invalidado"}), 200

# --------- Verificación de tokens en lista negra ---------
from src.app import jwt as jwt_manager

@jwt_manager.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload['jti'] in jwt_blacklist
