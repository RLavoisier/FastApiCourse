from enum import Enum

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response
from typing_extensions import Optional

from routers.blog.post import required_functionnality

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


@router.get(
    "/all",
    summary="get all the blogs",
    description="This endpoint allows you to fetch all the blogs",
    response_description="List of all available blog posts",
)
def get_all_blogs(
    page=1,
    page_size: Optional[int] = None,
    req_parameters: dict = Depends(required_functionnality),
):
    return {
        "message": f"All {page_size} blogs on page {page}",
        "req": req_parameters,
    }


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Retrieving a specific comment

    :param id: mandatory id parameter
    :param comment_id: the id f the comment
    :param valid: is the comment valid
    :param username: userame linked to the comment
    :return:
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}


@router.get("/test")
def get_test():
    return {"message": "test"}
