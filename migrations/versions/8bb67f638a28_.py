"""empty message

Revision ID: 8bb67f638a28
Revises: a2992d4a8756
Create Date: 2020-06-01 22:25:17.723706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bb67f638a28'
down_revision = 'a2992d4a8756'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('testing', sa.Integer(), nullable=True))
    op.add_column('labels', sa.Column('label', sa.Integer(), nullable=False))
    op.drop_column('labels', 'feedback_label')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('labels', sa.Column('feedback_label', sa.INTEGER(), nullable=False))
    op.drop_column('labels', 'label')
    op.drop_column('feedback', 'testing')
    # ### end Alembic commands ###