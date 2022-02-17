"""add last few columns to post table

Revision ID: 4f73bf522649
Revises: ef0201c120c4
Create Date: 2022-02-17 12:52:45.597092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f73bf522649'
down_revision = 'ef0201c120c4'
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
