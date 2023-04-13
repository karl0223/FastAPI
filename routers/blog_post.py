from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(prefix="/blog", tags=["blog"])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    body: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1: key2"}
    image: Optional[Image] = None


@router.post("/new/{id}")
def create_post(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment/{comment_id}}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: str = Query(
        None,
        title="Commnent Title",
        description="Description of the comment",
        alias="commentTitle",
        deprecated=True,
    ),
    content: str = Body(..., min_length=10, max_length=50, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
    comment_id: int = Path(..., gt=5, le=10),
):
    return {
        "id": id,
        "data": blog,
        "comment_title": comment_title,
        "content": content,
        "version": v,
    }
