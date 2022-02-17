"""add content column to post table

Revision ID: 7ec6128da54b
Revises: ff101e43eaad
Create Date: 2022-02-17 12:28:41.555056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ec6128da54b'
down_revision = 'ff101e43eaad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('post','content')
    pass
