from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..schemas import operation_schema as _schema
from ..crud import operation_crud as _crud
from ..dependencies import get_db

router = APIRouter(
    prefix="/operation"
)


@router.get("/all", response_model=List[_schema.Operation])
def read_operations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operations = _crud.get_operations(db, skip, limit)
    if not operations:
        raise HTTPException(status_code=404, detail="No operations found")
    return operations


@router.post("/create", response_model=_schema.Operation)
def create_operation(operation: _schema.OperationCreate, db: Session = Depends(get_db)):
    db_operation = _crud.get_operation_by_no(db, operation.operation_no)
    if db_operation:
        raise HTTPException(status_code=400, detail="Operation No. already exists in the database.")
    return _crud.add_operation(db, operation)


@router.get("/read/{operation_no}", response_model=_schema.Operation)
def read_operation_by_no(operation_no: str, db: Session = Depends(get_db)):
    db_operation = _crud.get_operation_by_no(db, operation_no)
    if db_operation is None:
        raise HTTPException(status_code=404, detail="Operation not found")
    return db_operation


@router.put("/update/{operation_no}", response_model=_schema.Operation)
def update_operation_by_no(operation_no: str, data: dict, db: Session = Depends(get_db)):
    db_operation = _crud.update_operation(db, operation_no, data)
    if db_operation is None:
        raise HTTPException(status_code=404, detail="Operation not found")
    return db_operation
