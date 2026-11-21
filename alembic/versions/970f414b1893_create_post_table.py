"""create post table

Revision ID: 970f414b1893
Revises: 
Create Date: 2026-11-20 22:59:39.377174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '970f414b1893'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('postsmukul',sa.Column('id',sa.Integer(), nullable=False , primary_key = True), 
                    sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('postsmukul')
    pass
