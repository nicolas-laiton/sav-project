# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials

# def check_google_drive_connection():
#     """
#     Verifica la conexión a Google Drive usando credenciales OAuth2.
#     """
#     # Cargar credenciales desde credentials.json (ajustar según tu flujo OAuth2)
#     creds = Credentials.from_authorized_user_file('assets/credentials.json', ['https://www.googleapis.com/auth/drive'])
#     service = build('drive', 'v3', credentials=creds)
    
#     # Intentar listar archivos como prueba de conexión
#     results = service.files().list(pageSize=1).execute()
#     return bool(results.get('files', []))  # Retorna True si hay acceso exitoso


import os
from google.oauth2.service_account import Credentials

def check_google_drive_connection():
    try:
        # Ruta al archivo JSON
        credentials_path = os.path.join("assets", "credentials.json")
        
        # Cargar las credenciales
        credentials = Credentials.from_service_account_file(credentials_path)
        
        # Validar que las credenciales sean válidas
        if credentials:
            return True
        else:
            return False
    except Exception as e:
        raise e
