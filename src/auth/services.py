from fastapi_mail import MessageSchema, MessageType
from src.core.mail import mail

async def send_welcome_email(recipients: list[str], subject: str, body: str):
    """
    Envía un correo usando FastMail.
    """
    message = MessageSchema(
        recipients=recipients,
        subject=subject,
        body=body,
        subtype=MessageType.html
    )

    await mail.send_message(message)