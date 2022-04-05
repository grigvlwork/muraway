import sqlalchemy
from .db_session import SqlAlchemyBase


class GroupUser(SqlAlchemyBase):
    __tablename__ = 'teacher_groups'

    group_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
