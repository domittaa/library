"""change to singular

Revision ID: 092cb88347a9
Revises: a22ed811c661
Create Date: 2024-02-29 13:01:04.516875

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "092cb88347a9"
down_revision: Union[str, None] = "a22ed811c661"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
