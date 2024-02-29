"""fix

Revision ID: 5260213c30d9
Revises: 8595f25dcd10
Create Date: 2024-02-29 12:49:41.202636

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5260213c30d9"
down_revision: Union[str, None] = "8595f25dcd10"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
