"""create post table

Revision ID: ff101e43eaad
Revises: 
Create Date: 2022-02-17 12:18:53.031909

"""
from tkinter.tix import Tree
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff101e43eaad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('post',sa.Column('id',sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('post')
    pass
