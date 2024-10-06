import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from openai import OpenAI

client = OpenAI(api_key='')

app = Flask(__name__)

# Set your OpenAI API key

# Sample data for doctors
doctors = [{'id': 1, 'name': 'Dr. Juan Pérez', 'specialty': 'Cardiólogo'}, 
           {'id': 2, 'name': 'Dra. María López', 'specialty': 'Neuróloga'}, 
           {'id': 3, 'name': 'Dr. Carlos García', 'specialty': 'Pediatra'}, 
           {'id': 4, 'name': 'Dra. Ana Fernández', 'specialty': 'Dermatóloga'}, 
           {'id': 5, 'name': 'Dr. Luis Rodríguez', 'specialty': 'Gastroenterólogo'}, 
           {'id': 6, 'name': 'Dra. Elena Sánchez', 'specialty': 'Ginecóloga'}, 
           {'id': 7, 'name': 'Dr. Miguel Martínez', 'specialty': 'Endocrinólogo'}, 
           {'id': 8, 'name': 'Dra. Laura Gómez', 'specialty': 'Oftalmóloga'}, 
           {'id': 9, 'name': 'Dr. José Torres', 'specialty': 'Psiquiatra'}, 
           {'id': 10, 'name': 'Dra. Sofía Díaz', 'specialty': 'Neumóloga'}, 
           {'id': 11, 'name': 'Dr. Alberto Romero', 'specialty': 'Oncólogo'}, 
           {'id': 12, 'name': 'Dra. Cristina Jiménez', 'specialty': 'Nefróloga'}, 
           {'id': 13, 'name': 'Dr. Francisco Moreno', 'specialty': 'Cirujano'}, 
           {'id': 14, 'name': 'Dra. Teresa Vega', 'specialty': 'Reumatóloga'}, 
           {'id': 15, 'name': 'Dr. Pablo Ruiz', 'specialty': 'Otorrinolaringólogo'}]

# Sample data for patients
patients = [
    {'id': 1, 'name': 'María García', 'pdf': 'maria_garcia.pdf', 'procedures': ['Cirugía de apéndice'], 'exams': ['Análisis de sangre'], 'medications': ['Ibuprofeno']},
    {'id': 2, 'name': 'Juan Pérez', 'pdf': 'juan_perez.pdf', 'procedures': ['Colocación de marcapasos'], 'exams': ['Electrocardiograma'], 'medications': ['Aspirina']},
    {'id': 3, 'name': 'Luisa Martínez', 'pdf': 'luisa_martinez.pdf', 'procedures': ['Extracción de muela'], 'exams': ['Radiografía dental'], 'medications': ['Amoxicilina']},
    {'id': 4, 'name': 'Carlos Rodríguez', 'pdf': 'carlos_rodriguez.pdf', 'procedures': ['Reemplazo de rodilla'], 'exams': ['Resonancia magnética'], 'medications': ['Paracetamol']},
    {'id': 5, 'name': 'Ana Sánchez', 'pdf': 'ana_sanchez.pdf', 'procedures': ['Cesárea'], 'exams': ['Ultrasonido'], 'medications': ['Oxitocina']},
    {'id': 6, 'name': 'José Fernández', 'pdf': 'jose_fernandez.pdf', 'procedures': ['Bypass gástrico'], 'exams': ['Endoscopia'], 'medications': ['Omeprazol']},
    {'id': 7, 'name': 'Laura Gómez', 'pdf': 'laura_gomez.pdf', 'procedures': ['Cirugía de cataratas'], 'exams': ['Examen de vista'], 'medications': ['Gotas oculares']},
    {'id': 8, 'name': 'Miguel Díaz', 'pdf': 'miguel_diaz.pdf', 'procedures': ['Reparación de hernia'], 'exams': ['Ecografía abdominal'], 'medications': ['Analgésicos']},
    {'id': 9, 'name': 'Elena Torres', 'pdf': 'elena_torres.pdf', 'procedures': ['Transplante de riñón'], 'exams': ['Análisis de orina'], 'medications': ['Inmunosupresores']},
    {'id': 10, 'name': 'Fernando Ruiz', 'pdf': 'fernando_ruiz.pdf', 'procedures': ['Artroscopia de hombro'], 'exams': ['Rayos X'], 'medications': ['Antiinflamatorios']},
    {'id': 11, 'name': 'Isabel Jiménez', 'pdf': 'isabel_jimenez.pdf', 'procedures': ['Cirugía láser ocular'], 'exams': ['Topografía corneal'], 'medications': ['Lágrimas artificiales']},
    {'id': 12, 'name': 'David Moreno', 'pdf': 'david_moreno.pdf', 'procedures': ['Angioplastia coronaria'], 'exams': ['Cateterismo cardíaco'], 'medications': ['Betabloqueantes']},
    {'id': 13, 'name': 'Sofía López', 'pdf': 'sofia_lopez.pdf', 'procedures': ['Amigdalectomía'], 'exams': ['Cultivo de garganta'], 'medications': ['Antibióticos']},
    {'id': 14, 'name': 'Antonio Hernández', 'pdf': 'antonio_hernandez.pdf', 'procedures': ['Prótesis de cadera'], 'exams': ['Densitometría ósea'], 'medications': ['Calcio']},
    {'id': 15, 'name': 'Carmen Navarro', 'pdf': 'carmen_navarro.pdf', 'procedures': ['Cirugía bariátrica'], 'exams': ['Prueba de tolerancia a la glucosa'], 'medications': ['Metformina']},
    {'id': 16, 'name': 'Jorge Castillo', 'pdf': 'jorge_castillo.pdf', 'procedures': ['Colecistectomía'], 'exams': ['Ecografía vesicular'], 'medications': ['Antiespasmódicos']},
    {'id': 17, 'name': 'Patricia Vega', 'pdf': 'patricia_vega.pdf', 'procedures': ['Cirugía de tiroides'], 'exams': ['Perfil tiroideo'], 'medications': ['Levotiroxina']},
    {'id': 18, 'name': 'Ricardo Molina', 'pdf': 'ricardo_molina.pdf', 'procedures': ['Cirugía de próstata'], 'exams': ['Antígeno prostático'], 'medications': ['Tamsulosina']},
    {'id': 19, 'name': 'Lucía Ramos', 'pdf': 'lucia_ramos.pdf', 'procedures': ['Reparación de válvula cardíaca'], 'exams': ['Ecocardiograma'], 'medications': ['Anticoagulantes']},
    {'id': 20, 'name': 'Francisco Romero', 'pdf': 'francisco_romero.pdf', 'procedures': ['Trasplante de hígado'], 'exams': ['Biopsia hepática'], 'medications': ['Ciclosporina']},
    {'id': 21, 'name': 'Sara Gil', 'pdf': 'sara_gil.pdf', 'procedures': ['Cirugía de columna'], 'exams': ['Tomografía axial computarizada'], 'medications': ['Relajantes musculares']},
    {'id': 22, 'name': 'Manuel Ortiz', 'pdf': 'manuel_ortiz.pdf', 'procedures': ['Cirugía de aneurisma'], 'exams': ['Angiografía'], 'medications': ['Estatinas']},
    {'id': 23, 'name': 'Clara Alonso', 'pdf': 'clara_alonso.pdf', 'procedures': ['Resección de tumor'], 'exams': ['Biopsia'], 'medications': ['Quimioterapia']},
    {'id': 24, 'name': 'Pedro Flores', 'pdf': 'pedro_flores.pdf', 'procedures': ['Cirugía de fístula'], 'exams': ['Colonoscopia'], 'medications': ['Antibióticos']}
]

appointments = []


@app.route('/')
def home():
    return render_template('home.html', doctors=doctors)


@app.route('/book/<int:doctor_id>', methods=['GET', 'POST'])
def book(doctor_id):
    doctor = next((doc for doc in doctors if doc['id'] == doctor_id), None)
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        appointments.append({'doctor': doctor, 'name': name, 'date': date})
        return redirect(url_for('home'))
    return render_template('book.html', doctor=doctor)


@app.route('/patients')
def patients_list():
    return render_template('patients.html', patients=patients)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'pdfs'), filename, as_attachment=True)


@app.route('/patient_details/<int:patient_id>')
def patient_details(patient_id):
    patient = next((pat for pat in patients if pat['id'] == patient_id), None)
    if patient:
        return jsonify(patient)
    return jsonify({'error': 'Patient not found'}), 404


@app.route('/authorize_medication', methods=['POST'])
def authorize_medication():
    data = request.json
    patient_id = data.get('patient_id')
    medication = data.get('medication')
    # Here you can add logic to handle the authorization request
    # For now, we'll just return a success message
    return jsonify({'message': f'Authorization requested for {medication} of patient {patient_id}'}), 200


@app.route('/book_procedure', methods=['POST'])
def book_procedure():
    data = request.json
    patient_id = data.get('patient_id')
    procedure = data.get('procedure')
    date = data.get('date')
    # Here you can add logic to handle the booking request
    # For now, we'll just return a success message
    return jsonify({'message': f'Procedure {procedure} booked for patient {patient_id} on {date}'}), 200


@app.route('/book_exam', methods=['POST'])
def book_exam():
    data = request.json
    patient_id = data.get('patient_id')
    exam = data.get('exam')
    date = data.get('date')
    # Here you can add logic to handle the booking request
    # For now, we'll just return a success message
    return jsonify({'message': f'Exam {exam} booked for patient {patient_id} on {date}'}), 200


@app.route('/appointments/<int:doctor_id>')
def view_appointments(doctor_id):
    doctor = next((doc for doc in doctors if doc['id'] == doctor_id), None)
    if not doctor:
        return "Doctor not found", 404
    doctor_appointments = [
        appt for appt in appointments if appt['doctor']['id'] == doctor_id]
    return render_template('appointments.html', doctor=doctor, appointments=doctor_appointments)


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=[
                                                      {"role": "system",
                                                          "content": "You are a helpful assistant."},
                                                      {"role": "user",
                                                          "content": user_message}
                                                  ])
        return jsonify({'response': response.choices[0].message.content.strip()})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'response': 'Sorry, something went wrong.'}), 500


@app.route('/chat_page')
def chat_page():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
