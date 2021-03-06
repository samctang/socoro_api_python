"""unique operation_no

Revision ID: 65210b3f37bf
Revises: 8cdd23676e05
Create Date: 2021-09-30 21:36:22.239689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65210b3f37bf'
down_revision = '8cdd23676e05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'operations', ['operation_no'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'operations', type_='unique')
    # ### end Alembic commands ###
