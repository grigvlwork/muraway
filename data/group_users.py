import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class GroupUser(SqlAlchemyBase):
    __tablename__ = 'group_users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id"),
                                 nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"),
                                nullable=False)
    user = orm.relation('User')
    group = orm.relation('Group')

