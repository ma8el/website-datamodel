"""Add greetings table

Revision ID: d4d39730656f
Revises: bae5498033c3
Create Date: 2023-03-06 19:26:25.858758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d39730656f'
down_revision = 'bae5498033c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('greeting',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('header', sa.Text(), nullable=False),
    sa.Column('sub_header', sa.Text(), nullable=False),
    sa.Column('image_ref', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('greeting')
    # ### end Alembic commands ###