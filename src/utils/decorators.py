from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from src.models.user_model import User

def role_required(*roles):
    """
    Protege un endpoint según los roles permitidos.
    Uso:
        @role_required('admin', 'user')
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # Verifica que haya un JWT válido
            verify_jwt_in_request()
            email = get_jwt_identity()
            user = User.query.filter_by(email=email).first()

            if not user:
                return jsonify({'msg': 'Usuario no encontrado'}), 404

            if user.role not in roles:
                return jsonify({'msg': 'Acceso denegado'}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
