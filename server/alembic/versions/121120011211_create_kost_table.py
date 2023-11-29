"""create kost table

Revision ID: 121120011211
Revises: 
Create Date: 2023-11-25 01:04:51.278092

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "121120011211"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "kost",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("price", sa.Integer, nullable=False),
        sa.Column("rating", sa.Integer, nullable=False),
        sa.Column("gender", sa.String(255), nullable=True),
        sa.Column("specification", sa.Text, nullable=True),
        sa.Column("rule", sa.Text, nullable=True),
        sa.Column("address", sa.Text, nullable=True),
        sa.Column("facility", sa.Text, nullable=False),
        sa.Column("image_url", sa.String(255), nullable=True),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table("kost")
