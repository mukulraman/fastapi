"""add user table

Revision ID: 56c7c95f726a
Revises: 53fabc6675e9
Create Date: 2026-11-20 23:41:31.556035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56c7c95f726a'
down_revision: Union[str, Sequence[str], None] = '53fabc6675e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
