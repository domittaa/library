"""pluar books

Revision ID: 92e80a5cf3ff
Revises: 092cb88347a9
Create Date: 2024-05-09 10:21:40.437596

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "92e80a5cf3ff"
down_revision: Union[str, None] = "092cb88347a9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
