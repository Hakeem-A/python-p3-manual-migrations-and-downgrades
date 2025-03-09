"""Renaming column in Student model

Revision ID: 39837e35939a
Revises: 791279dd0760
Create Date: 2025-03-09 13:51:21.904424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39837e35939a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='level')


def downgrade() -> None:
    op.alter_column('students', 'level', new_column_name='grade')
