"""empty message

Revision ID: 5ed723241ac7
Revises: 07ca18bf0451
Create Date: 2019-02-27 06:15:19.051935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ed723241ac7'
down_revision = '07ca18bf0451'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('todo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['todo_id'], ['todos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
