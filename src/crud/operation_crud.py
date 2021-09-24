from sqlalchemy.orm import Session
from ..schemas import operation_schema
from ..models import operation_model


def get_operations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(operation_model.Operation).order_by(operation_model.Operation.id.desc()).offset(skip).limit(limit).all()


def create_operation(db: Session, operation: operation_schema.OperationCreate):
    db_operation = operation_model.Operation(operation_no=operation.operation_no)  # add properties
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return db_operation
