"""fix back populates

Revision ID: 2b10280ac8b1
Revises: 92e80a5cf3ff
Create Date: 2024-05-09 10:30:56.904709

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2b10280ac8b1"
down_revision: Union[str, None] = "92e80a5cf3ff"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
