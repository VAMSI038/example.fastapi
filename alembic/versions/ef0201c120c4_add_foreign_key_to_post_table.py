"""add foreign-key to post table

Revision ID: ef0201c120c4
Revises: 0194bfb2bb3e
Create Date: 2022-02-17 12:43:59.621826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef0201c120c4'
down_revision = '0194bfb2bb3e'
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
