"""added languages field to Project model

Revision ID: cbaff20251e1
Revises: 4d8353b0c5d4
Create Date: 2024-11-04 12:42:10.766477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbaff20251e1'
down_revision = '4d8353b0c5d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('languages', sa.String(length=64), nullable=False))
        batch_op.create_index(batch_op.f('ix_project_languages'), ['languages'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_languages'))
        batch_op.drop_column('languages')

    # ### end Alembic commands ###