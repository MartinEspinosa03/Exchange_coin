# TIPO DE CAMBIO (USD/MXN)

El siguiente proyecto consta con una API de autenticación de usuarios y una base de datos SQLite

Características
------------ Registro y autenticación de usuarios.
# El sistema permite poder registrarse con sus datos personales como lo son: nombre de usuario, nombre, apellido, correo electrónico, contraseña.
# El sistema permite poder iniciar sesión con sus datos personales como lo son: nombre de usuario y contraseña.
# El sistema permite poder cerrar sesión.

------------ Manejo de tokens JWT.
# El sistema utiliza tokens JWT para acceder a la API de banxico y realizar la conversión de monedas con el valor actual hasta la fecha

------------ Base de datos con SQLite
# El sistema utiliza una base de datos SQLite para almacenar los datos de los usuarios registrados.

------------ Pruebas automatizadas
# El sistema cuenta con pruebas automatizadas para verificar la funcionalidad del registro de usuario.

Instalación
------------ Crear un entorno virtual e instalar dependencias

# python3 -m venv env

# source env/bin/activate

# $ pip3 install crispy-bootstrap5

# $ pip install requests beautifulsoup4

------------ Ejecutar la aplicación

# python3 manage.py migration
# python3 manage.py migrate
# python3 manage.py runserver
