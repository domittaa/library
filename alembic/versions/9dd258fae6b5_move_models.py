"""move models

Revision ID: 9dd258fae6b5
Revises: 9da6871d2809
Create Date: 2024-02-26 11:35:37.413581

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9dd258fae6b5"
down_revision: Union[str, None] = "9da6871d2809"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
