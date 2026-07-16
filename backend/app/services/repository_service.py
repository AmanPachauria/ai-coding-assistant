from fastapi import HTTPException
import re

def create_repository(url: str):

    if url == "":
        raise HTTPException(status_code = 400, detail = "Repository URL cannot be empty");

    github_pattern = r"^https://github\.com/[^/]+/[^/]+/?$"

    if not re.match(github_pattern, url):
        raise HTTPException(
            status_code=400,
            detail="Invalid GitHub repository URL."
        )
            

    return {
        "message": "Repository URL received successfully",
        "url": url
    }