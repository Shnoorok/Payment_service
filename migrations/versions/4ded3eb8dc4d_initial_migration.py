"""initial migration

Revision ID: 4ded3eb8dc4d
Revises:
Create Date: 2025-01-04 19:37:29.264268

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid

# revision identifiers, used by Alembic.
revision: str = '4ded3eb8dc4d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Создание таблицы payments
    op.create_table(
        'payments',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('currency', sa.String, nullable=False),
        sa.Column('status', sa.String, default='Pending'),
    )


def downgrade() -> None:
    # Удаление таблицы payments
    op.drop_table('payments')
    # ### end Alembic commands ###