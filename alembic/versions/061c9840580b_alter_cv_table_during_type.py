"""Alter cv table during type

Revision ID: 061c9840580b
Revises: 69a5ee081cbc
Create Date: 2023-03-13 23:15:21.627741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '061c9840580b'
down_revision = '69a5ee081cbc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('cv', 'during', type_=sa.Text)


def downgrade() -> None:
    op.alter_column('cv', 'during', type_=sa.Integer)
