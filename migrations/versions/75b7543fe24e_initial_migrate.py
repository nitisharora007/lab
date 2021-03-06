"""Initial migrate

Revision ID: 75b7543fe24e
Revises: 
Create Date: 2022-01-30 22:48:24.906210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75b7543fe24e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('roll_no', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=False),
    sa.Column('lname', sa.String(length=120), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('roll_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
