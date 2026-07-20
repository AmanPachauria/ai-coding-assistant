from fastapi import HTTPException
import re
import httpx


def validate_repository_url(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="Repository URL cannot be empty.")

    github_pattern = r"^https://github\.com/[^/]+/[^/]+/?$"

    if not re.match(github_pattern, url):
        raise HTTPException(status_code=400, detail="Invalid GitHub repository URL.")


def get_owner_and_repo_from_url(url: str):
    # remove trailing slash if present
    url = url.rstrip("/")
    
    # Split URL
    parts = url.split("/")
    
    owner = parts[-2]
    repository = parts[-1]

    return owner, repository

def fetch_repository_metadata(owner: str, repository: str):
    github_api_url = f"https://api.github.com/repos/{owner}/{repository}"
    response = httpx.get(github_api_url, follow_redirects=True)
    
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="GitHub repository not found.")
    
    repository_data  = response.json()

    return repository_data


def map_repository_response(repository_data: dict):
    return {
        "github_id": repository_data["id"],
        "owner": repository_data["owner"]["login"],
        "name": repository_data["name"],
        "description": repository_data["description"],
        "language": repository_data["language"],
        "stars": repository_data["stargazers_count"],
        "forks": repository_data["forks_count"],
        "default_branch": repository_data["default_branch"],
        "clone_url": repository_data["clone_url"]
    }


def create_repository(url: str):

    validate_repository_url(url) 

    owner, repository = get_owner_and_repo_from_url(url)
    
    repository_data = fetch_repository_metadata(owner, repository)

    return map_repository_response(repository_data)
