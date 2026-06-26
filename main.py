from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.ask import router as ask_router
from api.routes.users import router as users_router
from api.routes.company import router as company_router

# Create FastAPI app
app = FastAPI(
    title="Agent AI",
    version="1.0.0"
)

# Register routes
app.include_router(health_router, prefix="/health")
app.include_router(ask_router, prefix="/ask")
app.include_router(users_router, prefix="/users")
app.include_router(company_router, prefix="/company")


# Root endpoint (optional)
@app.get("/")
def root():
    return {"message": "Agent AI is running 🚀"}