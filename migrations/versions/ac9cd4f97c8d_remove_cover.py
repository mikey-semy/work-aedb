"""remove cover

Revision ID: ac9cd4f97c8d
Revises: 2ce5e439764d
Create Date: 2024-10-04 11:04:03.429442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac9cd4f97c8d'
down_revision: Union[str, None] = '2ce5e439764d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('manuals', 'cover_image_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manuals', sa.Column('cover_image_url', sa.VARCHAR(), nullable=False))
    # ### end Alembic commands ###
