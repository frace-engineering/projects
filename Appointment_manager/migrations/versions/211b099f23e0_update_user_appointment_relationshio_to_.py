"""Update User-Appointment relationshio to one-one

Revision ID: 211b099f23e0
Revises: 04f75e6e2de9
Create Date: 2024-07-20 20:39:28.778467

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '211b099f23e0'
down_revision = '04f75e6e2de9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=255),
               type_=sa.String(length=255, collation='utf8_general_ci'),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               type_=sa.String(length=50, collation='utf8_general_ci'),
               existing_nullable=False)
        batch_op.alter_column('first_name',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               type_=sa.String(length=50, collation='utf8_general_ci'),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               type_=sa.String(length=50, collation='utf8_general_ci'),
               existing_nullable=False)
        batch_op.alter_column('business_name',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               type_=sa.String(length=50, collation='utf8_general_ci'),
               existing_nullable=True)
        batch_op.alter_column('business_address',
               existing_type=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=200),
               type_=sa.String(length=200, collation='utf8_general_ci'),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('business_address',
               existing_type=sa.String(length=200, collation='utf8_general_ci'),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=200),
               existing_nullable=True)
        batch_op.alter_column('business_name',
               existing_type=sa.String(length=50, collation='utf8_general_ci'),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               existing_nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.String(length=50, collation='utf8_general_ci'),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               existing_nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.String(length=50, collation='utf8_general_ci'),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=50, collation='utf8_general_ci'),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=50),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=255, collation='utf8_general_ci'),
               type_=mysql.VARCHAR(charset='utf8mb3', collation='utf8mb3_general_ci', length=255),
               existing_nullable=False)

    # ### end Alembic commands ###
