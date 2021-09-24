from sqlalchemy import Column, String, DateTime


class Audit:
    last_modified_by = Column(String)
    last_modified_on = Column(DateTime)
    created_by = Column(String)
    created_on = Column(DateTime)
