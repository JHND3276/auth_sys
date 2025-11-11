from celery import Celery
from .settings import Config

def create_celery_app() -> Celery:
    app = Celery("auth_system")
    app.conf.update(
        broker_url = Config.RABBITMQ_URL,
        result_backend = Config.REDIS_URL,
        include = [
            # "src.aut.tasks",
        ],
        task_seriarizer = "json",
        accept_content=["json"],
        result_serializer="json",
        timezone="UTC",
        enable_utc=True,
        task_routes={
            #"src.auth.tasks.send_welcome_email_task":{"queue": "auth"},
        },
        worker_prefetch_multiplier=1,
        task_time_limit=300,
        task_soft_time_limit=120
    )
    return app