# Mutant DNA Detector

## Descripción

Este proyecto es una API que detecta si un ADN pertenece a un mutante basándose en patrones específicos. La API cuenta con un endpoint de detección de mutantes y otro de estadísticas, diseñada para identificar secuencias genéticas que corresponden a un mutante.

## Funcionalidades

- **Endpoint de Detección de Mutantes**: Permite enviar un ADN en formato JSON y verificar si corresponde a un mutante o no.
- **Endpoint de Estadísticas**: Muestra estadísticas sobre el número de solicitudes procesadas, el número de mutantes detectados y el número de humanos.

## Tecnologías utilizadas

- **Flask**: Framework web para la creación de la API.
- **Python 3.12**: Lenguaje de programación utilizado.
- **pytest**: Herramienta de pruebas para asegurar la calidad del código.
- **SQLite**: Base de datos utilizada para almacenar los datos de las detecciones.

## Instalación

Sigue los siguientes pasos para configurar el proyecto en tu máquina local:

### 1. Clonar el repositorio

`bash git clone https://github.com/usuario/mutant-dna-detector.git`

` cd mutant-dna-detector`
`

# 2. Crear un entorno virtual (opcional pero recomendado)`

` Se recomienda crear un entorno virtual para evitar conflictos con las dependencias del sistema. Para hacerlo, ejecuta:`

### En sistemas Linux/macOS

`python3 -m venv venv`

### En sistemas Windows

`python -m venv venv`

# 3. Activar el entorno virtual

### Linux/macOS:

`source venv/bin/activate`

### Windows:

`.\venv\Scripts\activate`

# 4. Instalar dependencias

`Instala todas las dependencias necesarias desde el archivo `

# requirements.txt:

`pip install -r requirements.txt`

# 5. Configuración de la base de datos

El proyecto utiliza SQLite para almacenar datos de las solicitudes de detección. Para crear la base de datos inicial, ejecuta el siguiente comando:

`python app/database.py`

Este comando generará el archivo dna_data.db en el directorio app/.

Ejecución
Para ejecutar la API localmente, utiliza el siguiente comando:

`python app/run.py`

Esto iniciará el servidor Flask en http://localhost:5000. Ahora puedes realizar solicitudes a los endpoints de la API.

# Pruebas

Para ejecutar las pruebas del proyecto, utiliza pytest. Las pruebas se encuentran en el directorio tests/. Para ejecutarlas, usa el siguiente comando:

`pytest tests/`

Esto ejecutará todas las pruebas del proyecto y te mostrará los resultados en la terminal.
