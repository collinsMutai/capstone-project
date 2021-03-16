"""empty message

Revision ID: 063d8900a731
Revises: fb1c7579ba62
Create Date: 2021-03-15 19:40:27.197833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '063d8900a731'
down_revision = 'fb1c7579ba62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'actor_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'actor_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###