from fastapi import FastAPI

from database import models
from database.engine import engine
from routers.article import router as article_router
from routers.blog.get import router as blog_router_get
from routers.blog.post import router as blog_router_post
from routers.user import router as user_router

app = FastAPI()
app.include_router(blog_router_get)
app.include_router(blog_router_post)
app.include_router(user_router)
app.include_router(article_router)


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


models.Base.metadata.create_all(bind=engine)
