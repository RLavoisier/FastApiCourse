from enum import Enum
from typing import Optional

from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


@app.get(
    "/blog/all",
    tags=["blog"],
    summary="get all the blogs",
    description="This endpoint allows you to fetch all the blogs",
    response_description="List of all available blog posts",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("blog/{id}/comments/{comment_id}", tags=["blog", "comment"])
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


@app.get("/blog/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}


@app.get("/blog/test", tags=["blog"])
def get_test():
    return {"message": "test"}
