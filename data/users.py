import datetime
import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase



class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # Фамилия
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # Имя
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    role = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)  # 0 - admin, 1 - teacher, 2 - pupil
