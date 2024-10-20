import uuid

from sqlalchemy.orm import Session

from database.models import DBArticle
from schemas import ArticleBase


def get_all_db_articles(db: Session):
    return db.query(DBArticle).all()


def create_db_article(db: Session, request: ArticleBase):
    new_article = DBArticle(
        title=request.title,
        user_id=request.user_id,
        content=request.content,
        published=request.published,
    )
    db.add(new_article)
    db.commit()


def get_article_by_id(db: Session, id: uuid.UUID):
    article = db.query(DBArticle).filter(DBArticle.id == id).first()
    return article
