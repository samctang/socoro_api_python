# from typing import List, Optional
import datetime
from pydantic import BaseModel


class OperationBase(BaseModel):
    company_id: int
    employee_id: int
    operation_no: str
    operation_type_id: int
    agent_id: int
    shipper_id: int
    consignee_id: int
    agent_ref_no: str
    shipper_ref_no: str
    consignee_ref_no: str
    port_of_loading: str
    port_of_departure: str
    origin_addr1: str
    origin_addr2: str
    origin_city: str
    origin_state: str
    origin_zip: str
    origin_country: str
    destination_addr1: str
    destination_addr2: str
    destination_city: str
    destination_state: str
    destination_zip: str
    destination_country: str
    carrier_id: int
    progress: int
    status: int
    submitted_date: datetime.datetime
    completed_date: datetime.datetime = None
    last_modified_by: str = None
    last_modified_on: datetime.datetime = None


class OperationCreate(OperationBase):
    created_by: str
    created_on: datetime.datetime


class Operation(OperationBase):
    id: int
    # processes: List[OperationProcess] = []

    class Config:
        orm_mode = True
