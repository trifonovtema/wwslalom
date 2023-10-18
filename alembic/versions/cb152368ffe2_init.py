"""init

Revision ID: cb152368ffe2
Revises: 
Create Date: 2023-10-17 02:29:36.168887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy

# revision identifiers, used by Alembic.
revision: str = 'cb152368ffe2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("create schema if not exists wwslalom")
    op.create_table('user',
    sa.Column('id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='wwslalom'
    )
    op.create_index(op.f('ix_wwslalom_user_email'), 'user', ['email'], unique=True, schema='wwslalom')
    op.create_table('user_details',
    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('surname', sa.String(length=1000), nullable=True),
    sa.Column('middle_name', sa.String(length=1000), nullable=True),
    sa.Column('telegram', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['wwslalom.user.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('user_id'),
    schema='wwslalom'
    )
    op.create_index(op.f('ix_wwslalom_user_details_middle_name'), 'user_details', ['middle_name'], unique=False, schema='wwslalom')
    op.create_index(op.f('ix_wwslalom_user_details_name'), 'user_details', ['name'], unique=False, schema='wwslalom')
    op.create_index(op.f('ix_wwslalom_user_details_surname'), 'user_details', ['surname'], unique=False, schema='wwslalom')
    op.create_index(op.f('ix_wwslalom_user_details_telegram'), 'user_details', ['telegram'], unique=False, schema='wwslalom')
    op.create_index(op.f('ix_wwslalom_user_details_user_id'), 'user_details', ['user_id'], unique=False, schema='wwslalom')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_wwslalom_user_details_user_id'), table_name='user_details', schema='wwslalom')
    op.drop_index(op.f('ix_wwslalom_user_details_telegram'), table_name='user_details', schema='wwslalom')
    op.drop_index(op.f('ix_wwslalom_user_details_surname'), table_name='user_details', schema='wwslalom')
    op.drop_index(op.f('ix_wwslalom_user_details_name'), table_name='user_details', schema='wwslalom')
    op.drop_index(op.f('ix_wwslalom_user_details_middle_name'), table_name='user_details', schema='wwslalom')
    op.drop_table('user_details', schema='wwslalom')
    op.drop_index(op.f('ix_wwslalom_user_email'), table_name='user', schema='wwslalom')
    op.drop_table('user', schema='wwslalom')
    op.execute("drop schema if exists wwslalom")
    # ### end Alembic commands ###