# Rock Instruments API 🎸🎶

**Rock Instruments API** es una aplicación web desarrollada con **Flask** y **SQLAlchemy** que permite gestionar un inventario de instrumentos musicales de manera eficiente. Este proyecto combina buenas prácticas de desarrollo web, interacción con bases de datos en la nube y un diseño moderno y minimalista.

---

## Definición y objetivo

El proyecto tiene como objetivo principal **facilitar la administración de instrumentos musicales**, proporcionando operaciones de **CRUD**:

- **Crear**: Añadir nuevos instrumentos al inventario.
- **Leer**: Visualizar la lista completa de instrumentos con detalles como nombre, tipo y marca.
- **Actualizar**: Modificar información existente de los instrumentos.
- **Eliminar**: Quitar instrumentos que ya no forman parte del inventario.

Esta funcionalidad permite a los usuarios mantener un registro actualizado y organizado de sus instrumentos, ideal para tiendas, escuelas de música o coleccionistas.

---

## Importancia del proyecto

1. **Gestión centralizada**: Permite almacenar toda la información de los instrumentos en una base de datos única, evitando registros dispersos o duplicados.  
2. **Eficiencia**: Automatiza tareas de registro y actualización de datos, reduciendo errores humanos.  
3. **Accesibilidad**: Al usar una base de datos en la nube, los datos son accesibles desde cualquier lugar y en cualquier momento.  
4. **Escalabilidad**: La aplicación puede crecer fácilmente agregando nuevas funcionalidades, como categorías, stock, precios, o integraciones con otros sistemas.  
5. **Aprendizaje y buenas prácticas**: El proyecto es útil para aprender conceptos fundamentales de desarrollo web en Python, manejo de bases de datos relacionales, diseño de interfaces modernas y despliegue en la nube.

---

## Características destacadas

- **Interfaz intuitiva y moderna**: Uso de tablas estilizadas, botones con hover y diseño minimalista para facilitar la navegación.  
- **Columna Marca**: Permite registrar información adicional de cada instrumento, lo que mejora el detalle y control del inventario.  
- **Operaciones completas de CRUD**: Garantiza que los usuarios puedan gestionar toda la información sin limitaciones.  
- **Conexión a base de datos en la nube**: Asegura que los datos se mantengan seguros y accesibles, promoviendo la colaboración y la continuidad del registro.

---

## Conclusión

**Rock Instruments API** no solo es un proyecto técnico, sino también una herramienta práctica para la gestión de inventarios musicales. Su desarrollo refuerza habilidades en **Flask, SQLAlchemy, diseño web y bases de datos en la nube**, mientras que su uso demuestra la importancia de contar con sistemas centralizados, escalables y accesibles para cualquier tipo de inventario.

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
