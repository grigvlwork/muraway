import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    board = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    background = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    example = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    goal = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_common = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False,
                                  default=False)
