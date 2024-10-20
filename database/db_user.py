import uuid

from sqlalchemy.orm import Session

from database.hash import Hash
from database.models import DBUser
from schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )

    db.add(new_user)
    db.commit()

    return new_user


def get_all_user(db: Session):
    return db.query(DBUser).all()


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(DBUser).filter(DBUser.id == user_id).first()


def update_user(db: Session, user_id: uuid.UUID, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == user_id)
    user.update(
        {
            DBUser.username: request.username,
            DBUser.email: request.email,
            DBUser.password: Hash.bcrypt(request.password),
        }
    )

    db.commit()


def delete_user(db: Session, user_id: uuid.UUID):
    db.delete(db.query(DBUser).filter(DBUser.id == user_id).first())
    db.commit()
