from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# create the tables
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


@app.get("/operations/", response_model=List[schemas.Operation])
def read_operations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operations = crud.get_operations(db, skip=skip, limit=limit)
    return operations

# Alembic is used for migrations

# run with: uvicorn socoro_api.main:app --reload
