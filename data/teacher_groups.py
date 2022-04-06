import sqlalchemy
from .db_session import SqlAlchemyBase


class TeacherGroup(SqlAlchemyBase):
    __tablename__ = 'teacher_groups'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    group_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
