from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from ..schemas import operation_schema
from ..crud import operation_crud
from ..dependencies import get_db


router = APIRouter(
    prefix="/operation"
)


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


@router.get("/", response_model=List[operation_schema.Operation])
def read_operations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operations = operation_crud.get_operations(db, skip=skip, limit=limit)
    return operations
