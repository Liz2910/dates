from flask_mail import Message

def enviar_correo(mail, nombre, telefono, fecha, hora, nota):
    try:
        msg = Message(
            subject="Nueva cita agendada",
            recipients=[mail.app.config["MAIL_USERNAME"]],
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
        print("✅ Correo enviado correctamente")
    except Exception as e:
        print("⚠️ Error al enviar correo:", e)
