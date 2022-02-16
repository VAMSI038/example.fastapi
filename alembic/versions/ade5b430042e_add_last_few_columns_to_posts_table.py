"""add last few columns to posts table

Revision ID: ade5b430042e
Revises: df7bab865c28
Create Date: 2022-02-16 16:34:16.707127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ade5b430042e'
down_revision = 'df7bab865c28'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('post',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text
        ('NOW()')),)
    pass


def downgrade():
    op.drop_column('post','published')
    op.drop_column('post','created_at')
    pass
