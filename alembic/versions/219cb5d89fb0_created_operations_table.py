"""created operations table

Revision ID: 219cb5d89fb0
Revises: 
Create Date: 2021-09-24 17:35:34.220205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '219cb5d89fb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###