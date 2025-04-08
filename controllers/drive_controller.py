import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def check_google_drive_connection():
    try:
        # Ruta al archivo JSON
        credentials_path = os.path.join("assets", "credentials.json")
        
        # Cargar las credenciales
        credentials = Credentials.from_service_account_file(
            credentials_path, 
            scopes=["https://www.googleapis.com/auth/drive"]
        )
        # Crear servicio
        service = build("drive", "v3", credentials=credentials)
        # Intentar listar archivos para verificar conexión
        service.files().list(pageSize=1).execute()
        return True
    except Exception as e:
        return False

def download_file_from_drive(drive_service, file_id, output_path):
    try:
        # Verificar la extensión para usar export en archivos de Google Workspace
        if output_path.endswith(".xlsx"):
            request = drive_service.files().export_media(fileId=file_id, mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            request = drive_service.files().get_media(fileId=file_id)
        
        with open(output_path, "wb") as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Progreso de descarga: {int(status.progress() * 100)}%")
        
        print(f"Archivo descargado correctamente en: {output_path}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")


def get_drive_service():
    """Inicializa y devuelve el servicio de Google Drive."""
    try:
        creds = Credentials.from_service_account_file(
            os.path.join("assets", "credentials.json"),
            scopes=["https://www.googleapis.com/auth/drive"]
        )
        return build("drive", "v3", credentials=creds)
    except Exception as e:
        raise Exception(f"Error al inicializar el servicio de Google Drive: {str(e)}")
