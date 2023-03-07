"""Add landing_socials table

Revision ID: bae5498033c3
Revises: 
Create Date: 2023-03-06 19:13:20.155390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bae5498033c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('landing_socials',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('icon', sa.Text(), nullable=False),
    sa.Column('href', sa.Text(), nullable=False),
    sa.Column('color', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('landing_socials')
    # ### end Alembic commands ###