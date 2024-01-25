"""upgrade jupyter-cache
Revision ID: 3b8cd69d4e4a
Revises: 
Create Date: 2024-01-25 15:35:46.072811

"""
from typing import Sequence, Union
from json import dumps
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b8cd69d4e4a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

default_read_data = {"name": "nbformat", "type": "plugin"}

def upgrade():
    op.rename_table(
        'nbstage',
        'nbproject',
    )
    with op.batch_alter_table("nbproject") as batch_op:
        batch_op.add_column(sa.Column('read_data', sa.JSON, nullable=False, server_default=dumps(default_read_data)))
        batch_op.add_column(sa.Column('exec_data', sa.JSON, nullable=True))

def downgrade():
    with op.batch_alter_table("nbproject") as batch_op:
        op.drop_column('read_data')
        op.drop_column('exec_data')
    op.rename_table(
        'nbproject',
        'nbstage',
    )
