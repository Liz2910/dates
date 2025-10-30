from flask_mail import Mail, Message
from flask import current_app

def enviar_correo(nombre, telefono, fecha, hora, nota):
    mail = Mail(current_app)
    msg = Message(
        subject="Nueva cita agendada",
        sender="lmcg2910@gmail.com",
        recipients=["lmcg2910@gmail.com"],
        body=f"""
        Se ha agendado una nueva cita:
        Nombre: {nombre}
        Teléfono: {telefono}
        Fecha: {fecha}
        Hora: {hora}
        Nota: {nota}
        """
    )

    mail.send(msg)
