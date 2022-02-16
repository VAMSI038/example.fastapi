"""create posts table

Revision ID: 7beaf1dcb9e4
Revises: 
Create Date: 2022-02-16 15:29:40.543449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7beaf1dcb9e4'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('post',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('post')
    pass
