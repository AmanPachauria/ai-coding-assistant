from fastapi import FastAPI

app = FastAPI(
    title="AI Coding Assistant API",
    version="1.0.0",
    description="Backend API for AI Coding Assistant"
)

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