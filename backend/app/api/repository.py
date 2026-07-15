from fastapi import APIRouter

from schemas.repository import RepositoryCreate

router = APIRouter()

@router.post("/repositories")
async def create_repository(repository: RepositoryCreate):
    return {
        "message": "Repository URL recieved successfully",
        "url": repository.url
    }