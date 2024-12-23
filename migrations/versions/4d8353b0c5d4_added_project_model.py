"""added Project model

Revision ID: 4d8353b0c5d4
Revises: 
Create Date: 2024-11-04 10:26:46.104735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d8353b0c5d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=False),
    sa.Column('gitRepoLink', sa.String(length=32), nullable=False),
    sa.Column('projectType', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_project_description'), ['description'], unique=True)
        batch_op.create_index(batch_op.f('ix_project_gitRepoLink'), ['gitRepoLink'], unique=True)
        batch_op.create_index(batch_op.f('ix_project_projectType'), ['projectType'], unique=True)
        batch_op.create_index(batch_op.f('ix_project_title'), ['title'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_project_title'))
        batch_op.drop_index(batch_op.f('ix_project_projectType'))
        batch_op.drop_index(batch_op.f('ix_project_gitRepoLink'))
        batch_op.drop_index(batch_op.f('ix_project_description'))

    op.drop_table('project')
    # ### end Alembic commands ###
