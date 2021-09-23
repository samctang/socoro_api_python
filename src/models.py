from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Audit:
    last_modified_by = Column(String)
    last_modified_on = Column(DateTime)
    created_by = Column(String)
    created_on = Column(DateTime)


class Operation(Base, Audit):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    # company_id = Column(Integer, ForeignKey("companies.id"))
    company_id = Column(Integer)
    employee_id = Column(Integer)
    operation_no = Column(String)
    operation_type_id = Column(Integer)
    agent_id = Column(Integer)
    shipper_id = Column(Integer)
    consignee_id = Column(Integer)
    agent_ref_no = Column(String)
    shipper_ref_no = Column(String)
    consignee_ref_no = Column(String)
    port_of_loading = Column(String)
    port_of_departure = Column(String)
    origin_addr1 = Column(String)
    origin_addr2 = Column(String)
    origin_city = Column(String)
    origin_state = Column(String)
    origin_zip = Column(String)
    origin_country = Column(String)
    destination_addr1 = Column(String)
    destination_addr2 = Column(String)
    destination_city = Column(String)
    destination_state = Column(String)
    destination_zip = Column(String)
    destination_country = Column(String)
    carrier_id = Column(Integer)
    progress = Column(Integer)
    status = Column(Integer)
    submitted_date = Column(DateTime)
    completed_date = Column(DateTime)

    # items = relationship("Item", back_populates="owner")


class OperationType(Base):
    __tablename__ = "operation_types"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    freight = Column(String)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="items")
