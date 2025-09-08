import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Crear la app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Modelo Instrumento
class Instrumento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))

# Crear la tabla automáticamente y agregar datos de prueba
with app.app_context():
    db.create_all()
    if not Instrumento.query.first():
        i1 = Instrumento(nombre="Guitarra", tipo="Cuerda")
        i2 = Instrumento(nombre="Batería", tipo="Percusión")
        i3 = Instrumento(nombre="Flauta", tipo="Viento")
        db.session.add_all([i1, i2, i3])
        db.session.commit()

# Listar instrumentos
@app.route("/")
def index():
    instrumentos = Instrumento.query.all()
    return render_template("index.html", instruments=instrumentos)

# Crear instrumento
@app.route("/create", methods=["GET", "POST"])
def create_instrument():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        tipo = request.form.get("tipo")
        nuevo_inst = Instrumento(nombre=nombre, tipo=tipo)
        db.session.add(nuevo_inst)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create_instrument.html")

# Editar instrumento
@app.route("/edit/<int:instrument_id>", methods=["GET", "POST"])
def edit_instrument(instrument_id):
    instrumento = Instrumento.query.get_or_404(instrument_id)
    if request.method == "POST":
        instrumento.nombre = request.form.get("nombre")
        instrumento.tipo = request.form.get("tipo")
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_instrument.html", instrumento=instrumento)

# Eliminar instrumento
@app.route("/delete/<int:instrument_id>")
def delete_instrument(instrument_id):
    instrumento = Instrumento.query.get_or_404(instrument_id)
    db.session.delete(instrumento)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5001)))
