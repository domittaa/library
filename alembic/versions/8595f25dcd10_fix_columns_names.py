"""fix columns names

Revision ID: 8595f25dcd10
Revises: 3eb7ddd46aec
Create Date: 2024-02-29 08:41:00.761770

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8595f25dcd10"
down_revision: Union[str, None] = "3eb7ddd46aec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
