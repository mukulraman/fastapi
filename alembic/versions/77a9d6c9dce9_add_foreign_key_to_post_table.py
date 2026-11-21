"""add foreign key to post table

Revision ID: 77a9d6c9dce9
Revises: 56c7c95f726a
Create Date: 2026-11-21 10:22:56.058010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77a9d6c9dce9'
down_revision: Union[str, Sequence[str], None] = '56c7c95f726a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('postsmukul', sa.Column('owner_id', sa.Integer(), nullable= False))
    op.create_foreign_key('post_user_fk', source_table='postsmukul', referent_table='posts1', local_cols=['owner_id'], 
                          remote_cols=['rate'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name='postsmukul', type_='foreignkey')
    op.drop_column('postsmukul', 'owner_id')
    pass
