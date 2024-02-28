"""rename secondary

Revision ID: bbb0fc85a316
Revises: 9dd258fae6b5
Create Date: 2024-02-28 14:21:48.271205

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bbb0fc85a316"
down_revision: Union[str, None] = "9dd258fae6b5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
