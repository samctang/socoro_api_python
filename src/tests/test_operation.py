import pytest
from src.tests.test_database import client, engine
from ..models.operation_model import Base


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)


def test_get_no_operations(test_db):
    response = client.get("/operation/all")
    assert response.status_code == 404


def test_create_operation(test_db):
    response = client.post(
        "/operation/create",
        json={"company_id": 0,
              "employee_id": 0,
              "operation_no": "string",
              "operation_type_id": 0,
              "agent_id": 0,
              "shipper_id": 0,
              "consignee_id": 0,
              "agent_ref_no": "string",
              "shipper_ref_no": "string",
              "consignee_ref_no": "string",
              "port_of_loading": "string",
              "port_of_departure": "string",
              "origin_addr1": "string",
              "origin_addr2": "string",
              "origin_city": "string",
              "origin_state": "string",
              "origin_zip": "string",
              "origin_country": "string",
              "destination_addr1": "string",
              "destination_addr2": "string",
              "destination_city": "string",
              "destination_state": "string",
              "destination_zip": "string",
              "destination_country": "string",
              "carrier_id": 0,
              "progress": 0,
              "status": 0,
              "submitted_date": "2021-10-01T02:01:46.330000",
              "completed_date": "2021-10-01T02:01:46.330000",
              "last_modified_by": "string",
              "last_modified_on": "2021-10-01T02:01:46.330000",
              "created_by": "string",
              "created_on": "2021-10-01T02:01:46.330000"})
    assert response.status_code == 200


def test_get_all_operations(test_db):
    response = client.get("/operation/all")
    assert response.status_code == 200


def test_create_error(test_db):
    response = client.post(
        "/operation/create",
        json={"company_id": 0,
              "employee_id": 0,
              "operation_no": "string",
              "operation_type_id": 0,
              "agent_id": 0,
              "shipper_id": 0,
              "consignee_id": 0,
              "agent_ref_no": "string",
              "shipper_ref_no": "string",
              "consignee_ref_no": "string",
              "port_of_loading": "string",
              "port_of_departure": "string",
              "origin_addr1": "string",
              "origin_addr2": "string",
              "origin_city": "string",
              "origin_state": "string",
              "origin_zip": "string",
              "origin_country": "string",
              "destination_addr1": "string",
              "destination_addr2": "string",
              "destination_city": "string",
              "destination_state": "string",
              "destination_zip": "string",
              "destination_country": "string",
              "carrier_id": 0,
              "progress": 0,
              "status": 0,
              "submitted_date": "2021-10-01T02:01:46.330000",
              "completed_date": "2021-10-01T02:01:46.330000",
              "last_modified_by": "string",
              "last_modified_on": "2021-10-01T02:01:46.330000",
              "created_by": "string",
              "created_on": "2021-10-01T02:01:46.330000"})
    assert response.status_code == 400


def test_get_operation_by_no(test_db):
    response = client.get("/operation/read/string")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "company_id": 0,
        "employee_id": 0,
        "operation_no": "string",
        "operation_type_id": 0,
        "agent_id": 0,
        "shipper_id": 0,
        "consignee_id": 0,
        "agent_ref_no": "string",
        "shipper_ref_no": "string",
        "consignee_ref_no": "string",
        "port_of_loading": "string",
        "port_of_departure": "string",
        "origin_addr1": "string",
        "origin_addr2": "string",
        "origin_city": "string",
        "origin_state": "string",
        "origin_zip": "string",
        "origin_country": "string",
        "destination_addr1": "string",
        "destination_addr2": "string",
        "destination_city": "string",
        "destination_state": "string",
        "destination_zip": "string",
        "destination_country": "string",
        "carrier_id": 0,
        "progress": 0,
        "status": 0,
        "submitted_date": "2021-10-01T02:01:46.330000",
        "completed_date": "2021-10-01T02:01:46.330000",
        "last_modified_by": "string",
        "last_modified_on": "2021-10-01T02:01:46.330000",
        "created_by": "string",
        "created_on": "2021-10-01T02:01:46.330000"
    }


def test_get_operation_by_no(test_db):
    response = client.get("/operation/read/fail")
    assert response.status_code == 404


def test_update_operation_by_no(test_db):
    response = client.put(
        "/operation/update/string",
        json={"employee_id": 2}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "company_id": 0,
        "employee_id": 2,
        "operation_no": "string",
        "operation_type_id": 0,
        "agent_id": 0,
        "shipper_id": 0,
        "consignee_id": 0,
        "agent_ref_no": "string",
        "shipper_ref_no": "string",
        "consignee_ref_no": "string",
        "port_of_loading": "string",
        "port_of_departure": "string",
        "origin_addr1": "string",
        "origin_addr2": "string",
        "origin_city": "string",
        "origin_state": "string",
        "origin_zip": "string",
        "origin_country": "string",
        "destination_addr1": "string",
        "destination_addr2": "string",
        "destination_city": "string",
        "destination_state": "string",
        "destination_zip": "string",
        "destination_country": "string",
        "carrier_id": 0,
        "progress": 0,
        "status": 0,
        "submitted_date": "2021-10-01T02:01:46.330000",
        "completed_date": "2021-10-01T02:01:46.330000",
        "last_modified_by": "string",
        "last_modified_on": "2021-10-01T02:01:46.330000",
        "created_by": "string",
        "created_on": "2021-10-01T02:01:46.330000"
    }


def test_update_operation_error(test_db):
    response = client.put(
        "/operation/update/fail",
        json={"employee_id": 2}
    )
    assert response.status_code == 404


def test_drop_db():
    Base.metadata.drop_all(bind=engine)
