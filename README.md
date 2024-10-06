# Gerencia de proyectos informaticos

Este proyecto es una aplicación web para gestionar citas médicas y proporcionar un asistente de chat para los pacientes. La aplicación está construida con Flask y utiliza la API de OpenAI para el asistente de chat.

## Requisitos

- Python 3.6 o superior
- Flask
- OpenAI

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/tuusuario/tu-repositorio.git](https://github.com/AntJyS/gerencia_proj_infa_22)
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configura tu clave de API de OpenAI:
   - Abre el archivo `app.py` y establece tu key de OpenAI en la variable `api_key`:
     ```python
     client = OpenAI(api_key='tu_clave_de_api')
     ```

4. Crea los directorios necesarios y coloca los archivos PDF de muestra:
   ```bash
   mkdir -p static/pdfs
   # Coloca tus archivos PDF en el directorio static/pdfs
   ```

## Ejecución

1. Inicia la aplicación Flask:
   ```bash
   python app.py
   ```

2. Abre tu navegador y navega a `http://localhost:5000` para ver la aplicación.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `templates/`: Directorio que contiene las plantillas HTML.
  - `home.html`: Página principal que muestra la lista de doctores.
  - `book.html`: Página para agendar una cita con un doctor.
  - `patients.html`: Página que muestra la lista de pacientes.
  - `patient_details.html`: Página que muestra los detalles de un paciente específico.
  - `chat.html`: Página del asistente de chat.
  - `appointments.html`: Página que muestra las citas con un doctor específico.
- `static/`: Directorio que contiene archivos estáticos como imágenes y PDFs.
  - `images/`: Directorio para las imágenes de fondo.
  - `pdfs/`: Directorio para los archivos PDF de los pacientes.

## Uso

1. **Lista de Doctores**:
   - Navega a la página principal para ver la lista de doctores disponibles.
   - Puedes agendar una cita o ver las citas existentes para cada doctor.

2. **Agendar Cita**:
   - Haz clic en "Agendar Cita" para un doctor específico y completa el formulario para agendar una cita.

3. **Lista de Pacientes**:
   - Navega a la página de pacientes para ver la lista de pacientes.
   - Haz clic en "Ver Detalles" para ver los detalles de un paciente específico, incluyendo sus procedimientos, exámenes y medicamentos.

4. **Asistente de Chat**:
   - Haz clic en "Chatea con nosotros" para abrir la página del asistente de chat y comunicarte con el asistente hospitalario.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para cualquier mejora o corrección.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```

### Explicación

1. **Requisitos**:
   - Lista los requisitos necesarios para ejecutar la aplicación.

2. **Instalación**:
   - Proporciona instrucciones paso a paso para clonar el repositorio, crear un entorno virtual, instalar dependencias y configurar la clave de API de OpenAI.

3. **Ejecución**:
   - Instrucciones para iniciar la aplicación Flask y acceder a ella en el navegador.

4. **Estructura del Proyecto**:
   - Describe la estructura del proyecto y el propósito de cada archivo/directorio.

5. **Uso**:
   - Explica cómo usar las diferentes funcionalidades de la aplicación.

6. **Contribuciones**:
   - Invita a otros a contribuir al proyecto.

7. **Licencia**:
   - Indica la licencia del proyecto.

Este README proporcionará a otros desarrolladores la información necesaria para replicar y ejecutar el proyecto en sus entornos locales.
