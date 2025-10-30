from googleapiclient.discovery import build
from google.oauth2 import service_account

def crear_evento(nombre, telefono, fecha, hora, nota):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'config/credentials.json'
    calendar_id = 'lmcg2910@gmail.com'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': f'Cita con {nombre}',
        'description': f'Teléfono: {telefono}\nNotas: {nota}',
        'start': {
            'dateTime': f'{fecha}T{hora}:00',
            'timeZone': 'America/Mexico_City',
        },
        'end': {
            'dateTime': f'{fecha}T{int(hora)+1}:00',
            'timeZone': 'America/Mexico_City',
        },
    }

    service.events().insert(calendarId=calendar_id, body=event).execute()
    print('Evento creado en Google Calendar')