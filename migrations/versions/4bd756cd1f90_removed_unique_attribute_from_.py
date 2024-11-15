"""removed unique attribute from projectType field in Project model

Revision ID: 4bd756cd1f90
Revises: 37ba4b97809b
Create Date: 2024-11-05 23:23:21.219731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bd756cd1f90'
down_revision = '37ba4b97809b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_index('ix_project_projectType')
        batch_op.create_index(batch_op.f('ix_project_projectType'), ['projectType'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_projectType'))
        batch_op.create_index('ix_project_projectType', ['projectType'], unique=1)

    # ### end Alembic commands ###