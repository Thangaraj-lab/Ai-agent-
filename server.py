# api/server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.logger import get_logger
from app.config import settings
from app.constants import APIRoutes

# Import routes
from api.routes.ask import router as ask_router
from api.routes.company import router as company_router
from api.routes.users import router as users_router
from api.routes.health import router as health_router


logger = get_logger(__name__)


def create_app() -> FastAPI:
    """
    Application factory (production best practice)
    """

    app = FastAPI(
        title=settings.APP_NAME,
        version="1.0.0",
        description="Agent AI Decision System"
    )

    # -------------------------------
    # 🔹 CORS CONFIG
    # -------------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # restrict in prod
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # -------------------------------
    # 🔹 REGISTER ROUTES
    # -------------------------------
    app.include_router(health_router, prefix=APIRoutes.HEALTH)
    app.include_router(ask_router, prefix=APIRoutes.ASK)
    app.include_router(users_router, prefix=APIRoutes.USERS)
    app.include_router(company_router, prefix=APIRoutes.COMPANY)

    logger.info("API server initialized")

    return app


# 🔥 App instance
app = create_app()