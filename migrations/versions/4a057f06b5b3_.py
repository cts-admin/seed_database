"""empty message

Revision ID: 4a057f06b5b3
Revises: 
Create Date: 2017-07-27 12:21:31.287280

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4a057f06b5b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('geo_location', 'district_name')
    op.drop_column('geo_location', 'fo_name')
    op.add_column('zone', sa.Column('district_name', sa.String(length=50), nullable=True))
    op.add_column('zone', sa.Column('fo_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('zone', 'fo_name')
    op.drop_column('zone', 'district_name')
    op.add_column('geo_location', sa.Column('fo_name', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('geo_location', sa.Column('district_name', mysql.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
