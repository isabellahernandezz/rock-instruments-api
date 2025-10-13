# 🎸 Rock Bands API

¡Bienvenido a la API más rockera del mundo! Este proyecto te permite gestionar bandas de rock, sus instrumentos y miembros, con autenticación segura y una interfaz web amigable.

---

## 📖 Descripción

La **Rock Bands API** es una aplicación web construida con Flask que permite realizar operaciones CRUD sobre bandas de rock y sus instrumentos. Incluye autenticación con JWT, una interfaz gráfica para editar datos, y está lista para ser desplegada en Railway.

---

## 🧰 Tecnologías usadas

| Tecnología   | Descripción                                 |
|-------------|---------------------------------------------|
| Python      | Lenguaje principal                          |
| Flask       | Framework web ligero                        |
| SQLAlchemy  | ORM para manejo de base de datos            |
| JWT         | Autenticación segura con tokens             |
| SQLite      | Base de datos local                         |
| Postman     | Pruebas de endpoints                        |

---

## ⚙️ Instalación paso a paso

1. 🔁 Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/rock-bands-api.git
   cd rock-bands-api
2. 🐍 Crea un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. 📦 Instala las dependencias:
pip install -r requirements.txt
4. 🔐 Configura las variables de entorno: Crea un archivo .env en la raíz con:
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
JWT_SECRET_KEY=tu_clave_jwt
5. 🚀 Corre la app en modo desarrollo:
flask run
📡 Uso de la API
🔗 Endpoints disponibles
Método	Ruta	Descripción
POST	/login	Autenticación de usuario
GET	/bands	Listar bandas
POST	/bands	Crear nueva banda
PUT	/bands/<id>	Editar banda
DELETE	/bands/<id>	Eliminar banda
GET	/instruments	Listar instrumentos
POST	/instruments	Crear instrumento
PUT	/instruments/<id>	Editar instrumento
DELETE	/instruments/<id>	Eliminar instrumento
🔐 Autenticación
Se requiere un token JWT para acceder a rutas protegidas.

Autenticarse vía /login con credenciales válidas.

El token debe enviarse en el header:Authorization: Bearer <tu_token>
🧪 Ejemplo de token JWT
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
🖥️ Interfaz web
La app incluye una interfaz gráfica construida con HTML/CSS/JS que permite:

Ver todas las bandas registradas.

Editar o eliminar bandas existentes.

Agregar nuevos instrumentos.

Navegación intuitiva y responsive.
🌿 Gestión de ramas y commits
main: rama estable para producción.

develop: rama de integración para nuevas funcionalidades.

feature/*: ramas individuales para cada nueva característica.
🧪 Pruebas
Las pruebas manuales se realizan con Postman e incluyen:

✅ Login y obtención de token.

🔒 Acceso a rutas protegidas.

🛠️ CRUD completo de bandas e instrumentos.

🧹 Validación de errores y respuestas.

📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.