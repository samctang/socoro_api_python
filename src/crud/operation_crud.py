from sqlalchemy.orm import Session
from ..schemas import operation_schema as _schema
from ..models import operation_model as _model


def get_operations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(_model.Operation).order_by(_model.Operation.id).offset(skip).limit(
        limit).all()


def add_operation(db: Session, operation: _schema.OperationCreate):
    db_operation = _model.Operation(**operation.dict())
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return db_operation


def get_operation_by_no(db: Session, operation_no: str):
    return db.query(_model.Operation).filter(_model.Operation.operation_no == operation_no).first()


def update_operation(db: Session, operation_no: str, data: dict):
    db_operation = db.query(_model.Operation).filter(_model.Operation.operation_no == operation_no)
    db_operation.update(data)
    db.commit()
    return db_operation.first()
