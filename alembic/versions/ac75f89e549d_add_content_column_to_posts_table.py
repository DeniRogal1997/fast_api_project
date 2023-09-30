"""add content column to posts table

Revision ID: ac75f89e549d
Revises: 007fe1f037da
Create Date: 2023-09-29 23:10:18.325059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ac75f89e549d'
down_revision: Union[str, None] = '007fe1f037da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
