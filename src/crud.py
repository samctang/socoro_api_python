from sqlalchemy.orm import Session

from . import models, schemas


def get_operations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operation).order_by(models.Operation.id.desc()).offset(skip).limit(limit).all()
