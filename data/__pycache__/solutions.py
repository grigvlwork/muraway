import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Solution(SqlAlchemyBase):
    __tablename__ = 'solutions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    task_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    commands = sqlalchemy.Column(sqlalchemy.String, nullable=True)
