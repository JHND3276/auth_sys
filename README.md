auth-system/
│
├── .env                          # Variables sensibles (no en git)
├── .gitignore
├── requirements.txt
├── docker-compose.yml            # Levanta RabbitMQ + Redis + app
│
├── settings/
│   ├── __init__.py
│   ├── config.py                 # Pydantic Settings (carga .env)
│   └── celery_config.py          # Config Celery (broker + backend)
│
├── src/
│   ├── __init__.py
│   │
│   ├── core/                     # Componentes compartidos
│   │   ├── __init__.py
│   │   ├── database.py           # AsyncSession (SQLAlchemy)
│   │   ├── security.py           # JWT, hash, verify
│   │   ├── mail.py               # FastMail + plantillas
│   │   └── redis.py              # Cliente Redis (cache + blacklist)
│   │
│   ├── auth/                     # Dominio de autenticación
│   │   ├── __init__.py
│   │   ├── models.py             # User, TokenBlacklist
│   │   ├── schemas.py            # Pydantic: UserCreate, Token, etc.
│   │   ├── services.py           # create_user(), authenticate(), send_welcome_email()
│   │   ├── tasks.py              # Celery: send_welcome_email_task()
│   │   └── routes.py             # /signup, /login, /refresh, /logout
│   │
│   └── roles/                    # (Opcional: roles, permisos)
│       ├── models.py
│       └── services.py
│
├── app.py                        # FastAPI app
├── celery_app.py                 # Instancia de Celery
├── main.py                       # Punto de entrada (uvicorn)
└── alembic/                      # Migraciones (SQLAlchemy)