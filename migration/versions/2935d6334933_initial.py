"""'Initial'

Revision ID: 2935d6334933
Revises: 
Create Date: 2023-06-17 03:59:39.844269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2935d6334933'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pack',
    sa.Column('id_pack', sa.Integer(), nullable=False),
    sa.Column('packname', sa.String(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id_pack')
    )
    op.create_table('dare',
    sa.Column('id_dare', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('id_pack', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_pack'], ['pack.id_pack'], ),
    sa.PrimaryKeyConstraint('id_dare')
    )
    op.create_table('truth',
    sa.Column('id_truth', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('id_pack', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_pack'], ['pack.id_pack'], ),
    sa.PrimaryKeyConstraint('id_truth')
    )
    op.create_table('dare_pack',
    sa.Column('id_pack', sa.Integer(), nullable=False),
    sa.Column('id_dare', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_dare'], ['dare.id_dare'], ),
    sa.ForeignKeyConstraint(['id_pack'], ['pack.id_pack'], ),
    sa.PrimaryKeyConstraint('id_pack', 'id_dare')
    )
    op.create_table('truth_pack',
    sa.Column('id_pack', sa.Integer(), nullable=False),
    sa.Column('id_truth', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_pack'], ['pack.id_pack'], ),
    sa.ForeignKeyConstraint(['id_truth'], ['truth.id_truth'], ),
    sa.PrimaryKeyConstraint('id_pack', 'id_truth')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('truth_pack')
    op.drop_table('dare_pack')
    op.drop_table('truth')
    op.drop_table('dare')
    op.drop_table('pack')
    op.drop_table('user')
    # ### end Alembic commands ###