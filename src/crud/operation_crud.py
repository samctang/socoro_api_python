from sqlalchemy.orm import Session
from ..schemas import operation_schema
from ..models import operation_model


def get_operations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(operation_model.Operation).order_by(operation_model.Operation.id.desc()).offset(skip).limit(
        limit).all()


def add_operation(db: Session, operation: operation_schema.OperationCreate):
    db_operation = operation_model.Operation(
        company_id=operation.company_id,
        operation_no=operation.operation_no,
        employee_id=operation.employee_id,
        operation_type_id=operation.operation_type_id,
        agent_id=operation.agent_id,
        shipper_id=operation.shipper_id,
        consignee_id=operation.consignee_id,
        agent_ref_no=operation.agent_ref_no,
        shipper_ref_no=operation.shipper_ref_no,
        consignee_ref_no=operation.consignee_ref_no,
        port_of_loading=operation.port_of_loading,
        port_of_departure=operation.port_of_departure,
        origin_addr1=operation.origin_addr1,
        origin_addr2=operation.origin_addr2,
        origin_city=operation.origin_city,
        origin_state=operation.origin_state,
        origin_zip=operation.origin_zip,
        origin_country=operation.origin_country,
        destination_addr1=operation.destination_addr1,
        destination_addr2=operation.destination_addr2,
        destination_city=operation.destination_city,
        destination_state=operation.destination_state,
        destination_zip=operation.destination_zip,
        destination_country=operation.destination_country,
        carrier_id=operation.carrier_id,
        progress=operation.progress,
        status=operation.status,
        submitted_date=operation.submitted_date,
        completed_date=operation.completed_date,
        last_modified_by=operation.last_modified_by,
        last_modified_on=operation.last_modified_on,
        created_by=operation.created_by,
        created_on=operation.created_on
    )
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return db_operation


def get_operation_by_no(db: Session, operation_no):
    return db.query(operation_model.Operation).where(operation_model.Operation.operation_no == operation_no)
