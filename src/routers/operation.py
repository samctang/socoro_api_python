from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..schemas import operation_schema
from ..crud import operation_crud
from ..dependencies import get_db

router = APIRouter(
    prefix="/operation"
)


@router.get("/all", response_model=List[operation_schema.Operation])
def read_operations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operations = operation_crud.get_operations(db, skip=skip, limit=limit)
    return operations


@router.post("/create", response_model=operation_schema.Operation)
def create_operation(operation: operation_schema.OperationCreate, db: Session = Depends(get_db)):
    # db_operation = operation_crud.get_operation_by_no(db, operation_no=operation.operation_no)
    # if db_operation:
    #    raise HTTPException(status_code=400, detail="Operation No. already exists in the database.")
    return operation_crud.add_operation(db=db, operation=operation)
