from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum

router = APIRouter(prefix="/blog", tags=["blog"])

# Default values
# @router.get("/blog/all")
# def get_blogs(page=1, page_size=10):
#     return {"message": f"all {page_size} blogs on page {page}"}


# Optional parameters
@router.get(
    "/all",
    summary="Retrieves all blogs",
    description="This API retrieves all blogs from the database",
    response_description="All blogs retrieved",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"all {page_size} blogs on page {page}"}


@router.get("/{id}/comments/{comment_id}", tags=["comments"])
def get_comments(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {"message": f"blog with id {id} has comment with id {comment_id}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"blog type is {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"blog with id {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"blog with id {id}"}


@router.get("/status/test/{id}")
def get_blog_status(id: int):
    if id > 5:
        return {"message": f"blog with id {id} not found"}
    else:
        return {"message": f"blog with id {id}"}
