"""add foreign-key to posts table

Revision ID: df7bab865c28
Revises: 8ea5934f9a51
Create Date: 2022-02-16 16:25:01.973341

"""
from tkinter import CASCADE
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df7bab865c28'
down_revision = '8ea5934f9a51'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="post",referent_table="users",
    local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name="post")
    op.drop_column('post','owner_id')
    pass
