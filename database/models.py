import uuid

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import UUID, Boolean, String

from database.engine import Base


class DBUser(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    articles = relationship("DBArticle", back_populates="user")


class DBArticle(Base):
    __tablename__ = "articles"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean)
    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("DBUser", back_populates="articles")
