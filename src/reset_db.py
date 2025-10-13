from src.app import db, create_app

# Crear la app y establecer el contexto
app = create_app()
with app.app_context():
    print("🔹 Eliminando todas las tablas...")
    db.drop_all()  # Elimina todas las tablas

    print("🔹 Creando todas las tablas nuevamente...")
    db.create_all()  # Crea las tablas según los modelos actuales

    print("✅ Base de datos reiniciada con éxito")
