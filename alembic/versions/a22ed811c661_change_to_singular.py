"""change to singular

Revision ID: a22ed811c661
Revises: 5260213c30d9
Create Date: 2024-02-29 12:59:11.187426

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a22ed811c661"
down_revision: Union[str, None] = "5260213c30d9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
