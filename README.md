# Rock Instruments API 🎸

Este proyecto es una **aplicación web en Flask** para gestionar una lista de **instrumentos musicales**, con CRUD completo (Crear, Leer, Actualizar, Eliminar) y diseño moderno y minimalista.

---

## Tecnologías usadas

- **Python 3.12**
- **Flask 3.0.3**
- **Flask-SQLAlchemy 3.0.5** para la interacción con la base de datos
- **PostgreSQL** (en la nube usando Railway)
- **Python-dotenv** para manejar variables de entorno
- **HTML y CSS** para las vistas, con un diseño moderno y minimalista

---

## Características

- Lista de instrumentos con columnas:
  - ID
  - Nombre
  - Tipo
  - Marca (nueva columna agregada)
  - Acciones (Editar / Eliminar)
- Formularios para **crear y editar instrumentos**.
- Diseño responsivo, limpio y moderno:
  - Tabla con sombras y bordes redondeados
  - Botones estilizados con hover
  - Colores suaves y agradables a la vista
- Conexión a **PostgreSQL en Railway**, para guardar los datos en la nube.

---

## Estructura del proyecto

rock-instruments-api/
├─ src/
│ ├─ app.py
│ ├─ static/
│ │ └─ style.css
│ └─ templates/
│ ├─ index.html
│ ├─ create_instrument.html
│ └─ edit_instrument.html
├─ .env # Contiene la URL de la base de datos y variables
├─ requirements.txt
└─ .gitignore



---

## Configuración local

1. Clonar el repositorio:

```bash
git clone https://github.com/tuusuario/rock-instruments-api.git
cd rock-instruments-api

Crear un entorno virtual:

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


Instalar dependencias:

pip install -r requirements.txt


Configurar .env con tu base de datos en Railway:

DATABASE_URL=postgres://usuario:contraseña@host:puerto/dbname
PORT=5001
FLASK_ENV=development


Ejecutar la aplicación:

python src/app.py


La app estará disponible en: http://localhost:5001

Notas

La columna Marca fue agregada después de la creación inicial del proyecto, tanto en el modelo como en la base de datos en Railway.

Todos los datos se guardan en la base de datos en la nube (Railway), por lo que puedes acceder a ellos desde cualquier lugar.

.gitignore incluye venv/, .env y archivos temporales para mantener el repositorio limpio.


