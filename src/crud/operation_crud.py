from sqlalchemy.orm import Session
from ..schemas import operation_schema
from ..models import operation_model


def get_operations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(operation_model.Operation).order_by(operation_model.Operation.id).offset(skip).limit(
        limit).all()


def add_operation(db: Session, operation: operation_schema.OperationCreate):
    db_operation = operation_model.Operation(**operation.dict())
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return db_operation


def get_operation_by_no(db: Session, operation_no):
    return db.query(operation_model.Operation).where(operation_model.Operation.operation_no == operation_no)
