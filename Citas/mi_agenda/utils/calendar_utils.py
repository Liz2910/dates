import os
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

def crear_evento(nombre, telefono, fecha, hora, nota):
    try:
        creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        creds = service_account.Credentials.from_service_account_info(
            creds_dict,
            scopes=["https://www.googleapis.com/auth/calendar"]
        )

        service = build("calendar", "v3", credentials=creds)

        event = {
            "summary": f"Cita con {nombre}",
            "description": f"Teléfono: {telefono}\nNotas: {nota}",
            "start": {
                "dateTime": f"{fecha}T{hora}:00",
                "timeZone": "America/Mexico_City"
            },
            "end": {
                "dateTime": f"{fecha}T{int(hora.split(':')[0])+1}:00",
                "timeZone": "America/Mexico_City"
            }
        }

        service.events().insert(calendarId="primary", body=event).execute()
        print("✅ Evento creado correctamente")
    except Exception as e:
        print("⚠️ Error al crear el evento:", e)
