from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from src.services.instrument_service import InstrumentService
from src.config.database import get_db_session


instrument_bp = Blueprint('instrument_bp', __name__)
service = InstrumentService(get_db_session())

# --------- API ---------
@instrument_bp.route('/api/instruments', methods=['GET'])
def get_instruments_api():
    instruments = service.listar_instruments()
    return jsonify([{'id': i.id, 'name': i.name, 'type': i.type} for i in instruments]), 200

@instrument_bp.route('/api/instruments/<int:instrument_id>', methods=['GET'])
def get_instrument_api(instrument_id):
    inst = service.obtener_instrument(instrument_id)
    if inst:
        return jsonify({'id': inst.id, 'name': inst.name, 'type': inst.type}), 200
    return jsonify({'error': 'Instrumento no encontrado'}), 404

# --------- Web ---------
@instrument_bp.route('/')
def home_page():
    instruments = service.listar_instruments()
    return render_template('index.html', instruments=instruments)

@instrument_bp.route('/create', methods=['GET', 'POST'])
def create_instrument_page():
    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        if name and type_:
            service.crear_instrument(name, type_)
            return redirect(url_for('instrument_bp.home_page'))
    return render_template('create_instrument.html')

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

@instrument_bp.route('/delete/<int:instrument_id>')
def delete_instrument_page(instrument_id):
    service.eliminar_instrument(instrument_id)
    return redirect(url_for('instrument_bp.home_page'))
