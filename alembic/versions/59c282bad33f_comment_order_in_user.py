"""comment order in user

Revision ID: 59c282bad33f
Revises: f645bd41bac7
Create Date: 2024-02-28 14:23:49.717150

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "59c282bad33f"
down_revision: Union[str, None] = "f645bd41bac7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
