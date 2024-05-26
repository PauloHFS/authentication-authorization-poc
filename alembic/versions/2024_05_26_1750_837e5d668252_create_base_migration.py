"""create base migration

Revision ID: 837e5d668252
Revises: 
Create Date: 2024-05-26 17:50:00.126271

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '837e5d668252'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('slug', sa.String(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('slug')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('client',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('organization_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['organization_id'], [
                                            'organization.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('organization_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['organization_id'], [
                                            'organization.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('membership',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('organization_id', sa.Integer(), nullable=False),
                    sa.Column('role_id', sa.Integer(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['organization_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('user_id', 'organization_id')
                    )
    op.create_table('permission',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('role_id', sa.Integer(), nullable=False),
                    sa.Column('resource', sa.String(), nullable=False),
                    sa.Column('can_create', sa.Boolean(), nullable=False),
                    sa.Column('can_read', sa.Boolean(), nullable=False),
                    sa.Column('can_update', sa.Boolean(), nullable=False),
                    sa.Column('can_delete', sa.Boolean(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('sale',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('client_id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('total', sa.Integer(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sale')
    op.drop_table('permission')
    op.drop_table('membership')
    op.drop_table('role')
    op.drop_table('client')
    op.drop_table('user')
    op.drop_table('organization')
    # ### end Alembic commands ###
