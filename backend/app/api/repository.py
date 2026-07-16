from fastapi import APIRouter

from app.schemas.repository import RepositoryCreate
from app.services.repository_service import create_repository

router = APIRouter()

@router.post("/repositories")
async def register_repository(repository: RepositoryCreate):
    return create_repository(repository.url)