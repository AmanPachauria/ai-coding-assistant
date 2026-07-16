from fastapi import FastAPI

from app.api.repository import router as repository_router

app = FastAPI(
    title="AI Coding Assistant API",
    version="1.0.0",
    description="Backend API for AI Coding Assistant"
)


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