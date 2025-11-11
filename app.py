# app.py
from fastapi import FastAPI
from src.auth.routes import router as auth_router
from src.auth.routes import router as test_router

app = FastAPI()

# Incluye las rutas de autenticación
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

# Opcional: también puedes crear una ruta global para pruebas
app.include_router(test_router, prefix="/api/v1", tags=["test"])