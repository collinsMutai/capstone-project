"""empty message

Revision ID: acf7b61b2544
Revises: 
Create Date: 2021-04-21 16:41:16.709132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acf7b61b2544'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('actors')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('actors_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('attributes_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='actors_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('movies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('attributes_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('release_date', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('actor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], name='movies_actor_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='movies_pkey')
    )
    # ### end Alembic commands ###
