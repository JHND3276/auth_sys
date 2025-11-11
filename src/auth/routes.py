# src/auth/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.auth.services import send_welcome_email

router = APIRouter()

# Modelo para la solicitud
class EmailRequest(BaseModel):
    recipients: list[str]
    subject: str
    body: str

@router.post("/send-test-email")
async def send_test_email(request: EmailRequest):
    """
    Endpoint para probar envío de correo directamente (sin Celery).
    """
    try:
        await send_welcome_email(
            recipients=request.recipients,
            subject=request.subject,
            body=request.body
        )
        return {"message": "Correo enviado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {str(e)}")