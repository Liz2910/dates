from flask import Flask, render_template, request, redirect, url_for
from utils.calendar_utils import crear_evento
from utils.email_utils import enviar_correo
from flask_mail import Mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com' # pyright: ignore[reportUndefinedVariable]
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lmcg2910@gmail.com' # type: ignore
app.config['MAIL_PASSWORD'] = 'ynpy uzor jugt cpzk'
app.config['MAIL_DEFAULT_SENDER'] = 'lmcg2910@gmail.com'

mail = Mail(app)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha = request.form['fecha']
    hora = request.form['hora']
    nota = request.form.get('nota', '')

    # Crear evento en Google Calendar
    crear_evento(nombre, telefono, fecha, hora, nota)

    # Enviar correo
    enviar_correo(mail, nombre, telefono, fecha, hora, nota)

    return render_template('confirmacion.html', nombre=nombre, fecha=fecha, hora=hora)

if __name__ == '__main__':
    app.run(debug=True)