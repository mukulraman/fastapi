"""add content to postsmukultable

Revision ID: 53fabc6675e9
Revises: 970f414b1893
Create Date: 2026-11-20 23:28:25.408951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53fabc6675e9'
down_revision: Union[str, Sequence[str], None] = '970f414b1893'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('postsmukul', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('postsmukul', 'content')
    pass
