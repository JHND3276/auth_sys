from celery_app import celery_app
from asgiref.sync import async_to_sync
from src.auth.services import send_welcome_email as send_welcome_email_impl

@celery_app.task(bind=True, max_retries=3, retry_backoff=True)
def send_welcome_email_task(self, email: str, token: str):
    """
    Tarea para enviar correo de bienvenida.
    """
    try:
        # Envuelve la función async en un contexto sync
        async_to_sync(send_welcome_email_impl)(email, token)
    except Exception as exc:
        # Reintenta la tarea si falla
        raise self.retry(exc=exc, countdown=60)  # Reintenta en 1 minuto