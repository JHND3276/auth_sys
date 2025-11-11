from celery_app import celery_app
from asgiref.sync import async_to_sync
from src.auth.services import send_welcome_email as send_welcome_email_impl

@celery_app.task
def send_test_email_task(recipients: list[str], subject: str, body: str):
    """
    Tarea para enviar un correo de prueba.
    """
    # Envuelve la función async en un contexto sync
    async_to_sync(send_welcome_email_impl)(recipients, subject, body)