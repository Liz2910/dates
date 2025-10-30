from flask import Flask, render_template, request
from flask_mail import Mail
from utils.calendar_utils import crear_evento
from utils.email_utils import enviar_correo
import os

app = Flask(__name__)

# Configuración del correo desde variables de entorno
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_USERNAME')
)

mail = Mail(app)

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

    # Enviar correo de confirmación
    enviar_correo(mail, nombre, telefono, fecha, hora, nota)

    return render_template('confirmacion.html', nombre=nombre, fecha=fecha, hora=hora)

if __name__ == '__main__':
    app.run(debug=True)
