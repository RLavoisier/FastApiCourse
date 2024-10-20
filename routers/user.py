import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import db_user
from database.engine import get_db
from schemas import UserBase, UserDisplay

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


# create
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# read
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)


@router.get("/{user_id}", response_model=UserDisplay)
def get_user_by_id(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return db_user.get_user(db, user_id)


# update
@router.put("/{user_id}")
def update_user(user_id: uuid.UUID, request: UserBase, db: Session = Depends(get_db)):
    db_user.update_user(db, user_id, request)


# delete
@router.delete("/{user_id}")
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user.delete_user(db, user_id)
