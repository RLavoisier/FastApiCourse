from datetime import datetime
from typing import Any, Dict, List

from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel
from typing_extensions import Optional

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    author: str
    published_on: Optional[datetime]
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, Any] = {}
    images: List[Image]


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version,
    }


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="Title of the comment",
        alias="commentTitle",
    ),
    content: str = Body(..., min_length=10, max_length=50, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(None, alias="version"),
    comment_id: int = Path(..., gt=5, le=10),
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id,
    }


def required_functionnality():
    return {"message": "learning fast api is important"}
