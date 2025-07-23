# Ikigai Web App

Esta aplicación de Flask permite explorar el concepto japonés de **Ikigai** mediante un pequeño ejercicio interactivo. Fue creada como proyecto para el curso CS50 de Harvard.

## Requisitos

- Python 3.8 o superior
- `pip` para instalar dependencias

## Instalación

1. Clona este repositorio.
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Define la variable de entorno `FLASK_APP`:
   ```bash
   export FLASK_APP=app.py
   ```
2. Inicia la aplicación con:
   ```bash
   flask run
   ```
3. Visita `http://127.0.0.1:5000/` en tu navegador para comenzar.

Los usuarios pueden registrarse, iniciar sesión y completar el formulario del ejercicio para guardar su Ikigai.

## Estructura

- `app.py` – Aplicación principal de Flask.
- `helpers.py` – Funciones auxiliares para la aplicación.
- `templates/` – Plantillas HTML.
- `static/` – Archivos estáticos (CSS y JavaScript).
- `project.db` – Base de datos SQLite con las tablas `users` e `ikigai_responses`.

> **Nota:** El archivo `project.db` se incluye solo con fines de desarrollo. Para un despliegue en producción se recomienda generar una base de datos nueva y configurar adecuadamente las credenciales.
