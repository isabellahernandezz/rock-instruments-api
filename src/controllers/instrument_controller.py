from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from services.instrument_service import InstrumentService
from config.database import get_db_session

# Creamos un Blueprint para organizar las rutas relacionadas con instrumentos
instrument_bp = Blueprint('instrument_bp', __name__)

# Instanciamos el servicio de instrumentos con una sesión de base de datos
service = InstrumentService(get_db_session())

# --------- Rutas API ---------

# Devuelve todos los instrumentos en formato JSON
@instrument_bp.route('/api/instruments', methods=['GET'])
def get_instruments_api():
    instruments = service.listar_instruments()
    return jsonify([{'id': i.id, 'name': i.name, 'type': i.type} for i in instruments]), 200

# Devuelve un instrumento específico por ID en formato JSON
@instrument_bp.route('/api/instruments/<int:instrument_id>', methods=['GET'])
def get_instrument_api(instrument_id):
    inst = service.obtener_instrument(instrument_id)
    if inst:
        return jsonify({'id': inst.id, 'name': inst.name, 'type': inst.type}), 200
    return jsonify({'error': 'Instrumento no encontrado'}), 404

# --------- Rutas Web ---------

# Página principal: muestra la lista de instrumentos en una tabla HTML
@instrument_bp.route('/')
def home_page():
    instruments = service.listar_instruments()
    return render_template('index.html', instruments=instruments)

# Página para crear un nuevo instrumento
# GET: muestra el formulario, POST: guarda el instrumento en la base de datos
@instrument_bp.route('/create', methods=['GET', 'POST'])
def create_instrument_page():
    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        if name and type_:
            service.crear_instrument(name, type_)
            return redirect(url_for('instrument_bp.home_page'))
    return render_template('create_instrument.html')

# Página para editar un instrumento existente
# GET: muestra los datos actuales, POST: actualiza la información
@instrument_bp.route('/edit/<int:instrument_id>', methods=['GET', 'POST'])
def edit_instrument_page(instrument_id):
    inst = service.obtener_instrument(instrument_id)
    if not inst:
        return "Instrumento no encontrado", 404

    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        service.actualizar_instrument(instrument_id, name, type_)
        return redirect(url_for('instrument_bp.home_page'))

    return render_template('edit_instrument.html', instrument=inst)

# Ruta para eliminar un instrumento por ID y redirigir a la página principal
@instrument_bp.route('/delete/<int:instrument_id>')
def delete_instrument_page(instrument_id):
    service.eliminar_instrument(instrument_id)
    return redirect(url_for('instrument_bp.home_page'))
