"""Create users and posts tables

Revision ID: 6415bf4f5f14
Revises: 3c632ea3a75d
Create Date: 2024-10-20 20:07:10.503127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6415bf4f5f14'
down_revision: Union[str, None] = '3c632ea3a75d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
