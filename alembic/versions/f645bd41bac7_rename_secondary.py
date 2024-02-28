"""rename secondary

Revision ID: f645bd41bac7
Revises: bbb0fc85a316
Create Date: 2024-02-28 14:22:48.911944

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f645bd41bac7"
down_revision: Union[str, None] = "bbb0fc85a316"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
