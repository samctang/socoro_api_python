"""added operations table

Revision ID: d10e9c34208b
Revises: b584d86c62cc
Create Date: 2021-09-23 01:33:31.883256

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'd10e9c34208b'
down_revision = 'b584d86c62cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('IX_OperationInsurances_OperationId', table_name='OperationInsurances')
    op.drop_table('OperationInsurances')
    op.drop_table('OperationContainerTypes')
    op.drop_table('CustomerTypes')
    op.drop_index('IX_EmployeeNotes_EmployeeId', table_name='EmployeeNotes')
    op.drop_table('EmployeeNotes')
    op.drop_index('IX_Carriers_CompanyId', table_name='Carriers')
    op.drop_table('Carriers')
    op.drop_index('IX_OperationTasks_OperationProcessId', table_name='OperationTasks')
    op.drop_table('OperationTasks')
    op.drop_index('IX_OperationProcesses_OperationId', table_name='OperationProcesses')
    op.drop_table('OperationProcesses')
    op.drop_table('AuditLogs')
    op.drop_index('IX_Operations_CompanyId', table_name='Operations')
    op.drop_index('IX_Operations_EmployeeId', table_name='Operations')
    op.drop_table('Operations')
    op.drop_index('IX_OperationQuotes_OperationId', table_name='OperationQuotes')
    op.drop_table('OperationQuotes')
    op.drop_index('IX_OperationBookings_OperationCargoId', table_name='OperationBookings')
    op.drop_table('OperationBookings')
    op.drop_index('IX_OperationContainers_OperationCargoId', table_name='OperationContainers')
    op.drop_table('OperationContainers')
    op.drop_index('IX_OperationBookingMessages_CarrierId', table_name='OperationBookingMessages')
    op.drop_index('IX_OperationBookingMessages_EmployeeId', table_name='OperationBookingMessages')
    op.drop_table('OperationBookingMessages')
    op.drop_index('IX_Employees_CompanyId', table_name='Employees')
    op.drop_table('Employees')
    op.drop_table('__EFMigrationsHistory')
    op.drop_table('CarrierTypes')
    op.drop_table('CompanyTypes')
    op.drop_table('OperationTypes')
    op.drop_index('IX_OperationCargos_OperationId', table_name='OperationCargos')
    op.drop_table('OperationCargos')
    op.drop_index('IX_Customers_CompanyId', table_name='Customers')
    op.drop_table('Customers')
    op.drop_table('OperationProcessTypes')
    op.drop_table('Departments')
    op.drop_table('Companies')
    op.create_table('operation_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('freight', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_types_id'), 'operation_types', ['id'], unique=False)
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('operation_no', sa.String(), nullable=True),
    sa.Column('operation_type_id', sa.Integer(), nullable=True),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.Column('shipper_id', sa.Integer(), nullable=True),
    sa.Column('consignee_id', sa.Integer(), nullable=True),
    sa.Column('agent_ref_no', sa.String(), nullable=True),
    sa.Column('shipper_ref_no', sa.String(), nullable=True),
    sa.Column('consignee_ref_no', sa.String(), nullable=True),
    sa.Column('port_of_loading', sa.String(), nullable=True),
    sa.Column('port_of_departure', sa.String(), nullable=True),
    sa.Column('origin_addr1', sa.String(), nullable=True),
    sa.Column('origin_addr2', sa.String(), nullable=True),
    sa.Column('origin_city', sa.String(), nullable=True),
    sa.Column('origin_state', sa.String(), nullable=True),
    sa.Column('origin_zip', sa.String(), nullable=True),
    sa.Column('origin_country', sa.String(), nullable=True),
    sa.Column('destination_addr1', sa.String(), nullable=True),
    sa.Column('destination_addr2', sa.String(), nullable=True),
    sa.Column('destination_city', sa.String(), nullable=True),
    sa.Column('destination_state', sa.String(), nullable=True),
    sa.Column('destination_zip', sa.String(), nullable=True),
    sa.Column('destination_country', sa.String(), nullable=True),
    sa.Column('carrier_id', sa.Integer(), nullable=True),
    sa.Column('progress', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('submitted_date', sa.DateTime(), nullable=True),
    sa.Column('completed_date', sa.DateTime(), nullable=True),
    sa.Column('last_modified_by', sa.String(), nullable=True),
    sa.Column('last_modified_on', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operations_id'), 'operations', ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operations_id'), table_name='operations')
    op.drop_table('operations')
    op.drop_index(op.f('ix_operation_types_id'), table_name='operation_types')
    op.drop_table('operation_types')
    op.create_table('Companies',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('TypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('CompanyName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CompanyName2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CompanyDBA', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CompanyDBA2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('EIN', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('NoEmployees', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_Companies')
    )
    op.create_table('Departments',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_Departments')
    )
    op.create_table('OperationProcessTypes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('OperationTypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Process', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationProcessTypes')
    )
    op.create_table('Customers',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('TypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Email', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CompanyName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ContactPhone', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('FirstName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MiddleName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DocumentalEmail', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CompanyId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_Customers')
    )
    op.create_index('IX_Customers_CompanyId', 'Customers', ['CompanyId'], unique=False)
    op.create_table('OperationCargos',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('LoadingAddress', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ContactEmail', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ContactPhone', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LoadingDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LoadingTime', mssql.TIME(), autoincrement=False, nullable=False),
    sa.Column('Reference', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('EIN', sa.INTEGER(), server_default=sa.text('((0))'), autoincrement=False, nullable=False),
    sa.Column('Bonded', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('Propelled', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('NoContainers', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('OperationId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationCargos')
    )
    op.create_index('IX_OperationCargos_OperationId', 'OperationCargos', ['OperationId'], unique=False)
    op.create_table('OperationTypes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Freight', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationTypes')
    )
    op.create_table('CompanyTypes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_CompanyTypes')
    )
    op.create_table('CarrierTypes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_CarrierTypes')
    )
    op.create_table('__EFMigrationsHistory',
    sa.Column('MigrationId', sa.NVARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('ProductVersion', sa.NVARCHAR(length=32), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('MigrationId', name='PK___EFMigrationsHistory')
    )
    op.create_table('Employees',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('DepartmentId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('EmployerId', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('FirstName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MiddleName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('WorkPhone', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MobilePhone', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MailZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DoB', mssql.DATETIME2(), server_default=sa.text("('0001-01-01T00:00:00.0000000')"), autoincrement=False, nullable=False),
    sa.Column('Gender', sa.NVARCHAR(length=1), autoincrement=False, nullable=False),
    sa.Column('HireDate', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.Column('CompanyId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_Employees')
    )
    op.create_index('IX_Employees_CompanyId', 'Employees', ['CompanyId'], unique=False)
    op.create_table('OperationBookingMessages',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('EmployeeId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CarrierId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Message', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationBookingMessages')
    )
    op.create_index('IX_OperationBookingMessages_EmployeeId', 'OperationBookingMessages', ['EmployeeId'], unique=False)
    op.create_index('IX_OperationBookingMessages_CarrierId', 'OperationBookingMessages', ['CarrierId'], unique=False)
    op.create_table('OperationContainers',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('TypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('GrossWeight', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('CommercialDescription', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Hazardous', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('HazardClass', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('UNCode', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ContainerNo', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('SealNo', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('TareWeight', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('OperationCargoId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.Column('Commodities', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Marks', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationContainers')
    )
    op.create_index('IX_OperationContainers_OperationCargoId', 'OperationContainers', ['OperationCargoId'], unique=False)
    op.create_table('OperationBookings',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('BookingNumber', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Vessel', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Voyage', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('DocumentDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('DocumentTime', mssql.TIME(), autoincrement=False, nullable=False),
    sa.Column('CargoDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('CargoTime', mssql.TIME(), autoincrement=False, nullable=False),
    sa.Column('VGMDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('DepartureDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('ArrivalDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('Ramp', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('RampDate', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('OperationCargoId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationBookings')
    )
    op.create_index('IX_OperationBookings_OperationCargoId', 'OperationBookings', ['OperationCargoId'], unique=False)
    op.create_table('OperationQuotes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Profit', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Documentation', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('FF', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('VGM', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Inland', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Others', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Explanation', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OperationId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationQuotes')
    )
    op.create_index('IX_OperationQuotes_OperationId', 'OperationQuotes', ['OperationId'], unique=False)
    op.create_table('Operations',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('OperationNo', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('TypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Agent', sa.INTEGER(), server_default=sa.text('((0))'), autoincrement=False, nullable=False),
    sa.Column('Shipper', sa.INTEGER(), server_default=sa.text('((0))'), autoincrement=False, nullable=False),
    sa.Column('Consignee', sa.INTEGER(), server_default=sa.text('((0))'), autoincrement=False, nullable=False),
    sa.Column('AgentRefNo', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ShipperRefNo', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ConsigneeRefNo', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PoL', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PoD', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OriginAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OriginAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OriginCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OriginState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OriginZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OriginCountry', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DestinationAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DestinationAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DestinationCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DestinationState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DestinationZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DestinationCountry', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Progress', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Status', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('SubmittedDate', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.Column('CompletedDate', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.Column('CompanyId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('EmployeeId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.Column('Carrier', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_Operations')
    )
    op.create_index('IX_Operations_EmployeeId', 'Operations', ['EmployeeId'], unique=False)
    op.create_index('IX_Operations_CompanyId', 'Operations', ['CompanyId'], unique=False)
    op.create_table('AuditLogs',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('UserId', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Type', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('TableName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DateTime', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('OldValues', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('NewValues', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('AffectedColumns', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PrimaryKey', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_AuditLogs')
    )
    op.create_table('OperationProcesses',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('TypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Status', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('OperationId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationProcesses')
    )
    op.create_index('IX_OperationProcesses_OperationId', 'OperationProcesses', ['OperationId'], unique=False)
    op.create_table('OperationTasks',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Note', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DueDate', mssql.DATETIME2(), server_default=sa.text("('0001-01-01T00:00:00.0000000')"), autoincrement=False, nullable=False),
    sa.Column('Status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('OperationProcessId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationTasks')
    )
    op.create_index('IX_OperationTasks_OperationProcessId', 'OperationTasks', ['OperationProcessId'], unique=False)
    op.create_table('Carriers',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('TypeId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('CarrierName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Phone', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhoneExt', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('FirstName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MiddleName', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr1', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyAddr2', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyCity', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyState', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('PhyZip', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DirectConnection', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('CompanyId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_Carriers')
    )
    op.create_index('IX_Carriers_CompanyId', 'Carriers', ['CompanyId'], unique=False)
    op.create_table('EmployeeNotes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('EmployeeId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_EmployeeNotes')
    )
    op.create_index('IX_EmployeeNotes_EmployeeId', 'EmployeeNotes', ['EmployeeId'], unique=False)
    op.create_table('CustomerTypes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_CustomerTypes')
    )
    op.create_table('OperationContainerTypes',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Description', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationContainerTypes')
    )
    op.create_table('OperationInsurances',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Value', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Freight', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Duties', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('OtherCosts', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('VoluntaryCoverage', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('LostProfit', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('OperationId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CreatedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('CreatedOn', mssql.DATETIME2(), autoincrement=False, nullable=False),
    sa.Column('LastModifiedBy', sa.NVARCHAR(), autoincrement=False, nullable=True),
    sa.Column('LastModifiedOn', mssql.DATETIME2(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='PK_OperationInsurances')
    )
    op.create_index('IX_OperationInsurances_OperationId', 'OperationInsurances', ['OperationId'], unique=False)

    # ### end Alembic commands ###