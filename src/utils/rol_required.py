from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.models.user_model import User

def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            identity = get_jwt_identity()
            user = User.query.filter_by(email=identity).first()
            if not user or user.role != required_role:
                return jsonify({'msg': 'Acceso denegado, rol insuficiente'}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
