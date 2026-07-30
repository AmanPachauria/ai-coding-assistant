from fastapi import FastAPI

from app.api.repository import router as repository_router

# Database Imports
from app.database.database import Base, engine

# Import all models so SQLAlchemy knows about them
from app.models.repository import Repository


app = FastAPI(
    title="AI Coding Assistant API",
    version="1.0.0",
    description="Backend API for AI Coding Assistant"
)

# Create database tables (only if they don't already exist)
Base.metadata.create_all(bind=engine)

# Register API Routes
app.include_router(repository_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to AI Coding Assistant"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }