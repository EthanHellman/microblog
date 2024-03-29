"""new fiels in user modedel

Revision ID: 24de8f0421c1
Revises: f6b212ea731c
Create Date: 2019-12-08 14:06:33.456924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24de8f0421c1'
down_revision = 'f6b212ea731c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
