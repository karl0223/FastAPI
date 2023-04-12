from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    body: str
    nb_comments: int
    published: Optional[bool] = None


@router.post("/new")
def create_post(blog: BlogModel):
    return {"data": blog}
