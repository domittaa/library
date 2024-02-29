"""add orders

Revision ID: 3eb7ddd46aec
Revises: 59c282bad33f
Create Date: 2024-02-29 08:38:54.673545

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3eb7ddd46aec"
down_revision: Union[str, None] = "59c282bad33f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
