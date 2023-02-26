"""add total_votes column

Revision ID: 3270898bfb34
Revises: 5f68459a94bb
Create Date: 2023-02-26 05:37:21.643356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3270898bfb34'
down_revision = '5f68459a94bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vibes', sa.Column('total_votes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vibes', 'total_votes')
    # ### end Alembic commands ###
