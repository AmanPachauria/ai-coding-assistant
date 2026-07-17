from fastapi import HTTPException
import re
import httpx

def create_repository(url: str):

    if url == "":
        raise HTTPException(status_code = 400, detail = "Repository URL cannot be empty");

    github_pattern = r"^https://github\.com/[^/]+/[^/]+/?$"

    if not re.match(github_pattern, url):
        raise HTTPException( status_code=400, detail="Invalid GitHub repository URL." )
    
    # remove trailing slash if present
    url = url.rstrip("/")
    
    # Split URL
    parts = url.split("/")
    
    owner = parts[-2]
    repository = parts[-1]

    github_api_url = f"https://api.github.com/repos/{owner}/{repository}"

    response = httpx.get(github_api_url, follow_redirects=True);
    
    return response.json()

    return {
        "message": "Repository URL received successfully",
        "url": url
    }