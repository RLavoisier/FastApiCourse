import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db_article import (
    create_db_article,
    get_all_db_articles,
    get_article_by_id,
)
from database.engine import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter(
    prefix="/article",
    tags=["article"],
)


@router.get("/", response_model=List[ArticleDisplay])
async def get_all_articles(db: Session = Depends(get_db)):
    return get_all_db_articles(db)


@router.get("/{article_id}", response_model=ArticleDisplay)
async def get_article(article_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_article_by_id(db, article_id)


@router.post("/")
async def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    create_db_article(db, request)
