"""add content column to post table

Revision ID: 7290b3dc1114
Revises: 7beaf1dcb9e4
Create Date: 2022-02-16 15:57:03.394960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7290b3dc1114'
down_revision = '7beaf1dcb9e4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('post','content')
    pass
