# Chatbot 'Elige tu propia aventura' API

[![Check code lint](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/lint.yml/badge.svg)](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/lint.yml)
[![Run tests](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/test.yml/badge.svg)](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/test.yml)
[![Build and test container](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/test-container.yml/badge.svg)](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/test-container.yml)
[![Deploy](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/deploy.yml/badge.svg)](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/actions/workflows/deploy.yml)


## Descripción

Esta API permite a los usuarios interactuar con un chatbot que simula una aventura interactiva al estilo "Elige tu propia aventura". 
Los usuarios pueden iniciar aventuras y elegir opciones que afecten el desarrollo de la historia.
(Elegir la opcion de PHP, recomendado :flushed:)

Se realizó el desarrollo en base a los siguientes [requerimientos](https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura/requerimientos-backend-api.pdf)

Aclaración: Es la primera vez que utilizó Flask.

### Extras

- Se agregaron validaciones con Pydantic
- Se agregó Swagger para documentar los enpoints (muy basico igual)
- Se configuraon GitHub Actions para test, formatear y verificar el codigo
- Se realizo el deploy en Vercel para facilitar su prueba.
- Se agregron migraciones.

## Tecnologías utilizadas

- **Flask**: Framework.
- **Flasgger**: Documentación de API basada en Swagger.
- **Pydantic**: Validación de datos y modelos.
- **Docker**: Contenerización de la aplicación y GitHub Actions.
- **Postman**: Probar la API.

# Guía para Correr la API Localmente

## Requisitos Previos

Antes de empezar, asegúrate de tener instalados los siguientes programas en tu máquina:

### Para correr con Docker
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Para correr sin Docker
- Python 3 y pip, terminal para correr `run.sh`.

**Clona el Repositorio**:
   - Abre una terminal y clona el repositorio donde se encuentra tu API:
     ```bash
     git clone https://github.com/leandrocarriego/chatbot-api-elige-tu-aventura
     cd chatbot-api-elige-tu-aventura
     ```
   - Cambiar el nombre del archivo .env.example por .env

## Correr la API con Docker Compose

1. **Construir y Levantar los Contenedores**:
   - Encender Docker
   - En la terminal, ejecuta el siguiente comando para construir y levantar la API:
     ```bash
     docker-compose up --build
     ```

2. **Acceder a la API**:
   - Una vez que los contenedores estén en funcionamiento, abre el navegador y visita:
     ```
     http://localhost:5000/docs
     ```
   - Acá se pueden probar los endpoints de tu API a través de la interfaz de Swagger o sino podes usar Postman.

## Correr la API con `run.sh`

1. **Ejecutar el Script**:
   - En la terminal, ejecuta el script para iniciar la API:
     ```bash
     sh /run.sh
     ```
   - Seleccionar sistema operativo + Enter

4. **Acceder a la API**:
   - Una vez que la API esté en funcionamiento, abre tu navegador y visita:
     ```
     http://localhost:5000/docs
     ```
   - Acá se pueden probar los endpoints de tu API a través de la interfaz de Swagger o sino podes usar Postman.

# Guía para Probar la API desplegada en Vercel

- Endpoints:
     - `GET /docs`: Para acceder a la documentacion de Swagger.
     - `GET /api/v1/`: Para verificar el funcionamiento de la API.
     - `POST /api/v1/start`: Para iniciar una nueva aventura.
     - `POST /api/v1/choose`: Para elegir una opción en la aventura.

## Probar la API en Vercel

1. **Acceder a la documentación de Swagger**:
     ```
     https://chatbot-api-elige-tu-aventura.vercel.app/docs/
     ```
   - Seleccionar `HTTPS`
   - Desde acá se pueden probar los endpoints directamente desde la interfaz de Swagger.

## Probar la API con Postman


2. **Agregar Solicitudes a la Colección**:

   - **Inicio de aventura**:
     - Método: `POST`
     - URL: 
       ```
       https://chatbot-api-elige-tu-aventura.vercel.app/api/v1/start
       ```
     - Body (JSON):
       ```json
       {}
       ```

   - **Elegir opción**:
     - Método: `POST`
     - URL: 
       ```
       https://chatbot-api-elige-tu-aventura.vercel.app/api/v1/choose
       ```
     - Body (JSON):
       ```json
       {
           "option_id": "opción_elegida"
       }
       ```
     - Reemplaza `"opción_elegida"` con la opción que deseas elegir en la aventura.

