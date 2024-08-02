# models/user.py
from .db import db, BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    display_name = db.Column(db.String(80), nullable=True)
    avatar_url = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    @classmethod
    def auth(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user is None:
            raise UserExceptions.UserNotFound
        if AuthModel.verify_password(user.id, password):
            return user
        else:
            raise UserExceptions.InvalidPassword


class UserExceptions:
    class UserNotFound(Exception):
        pass

    class InvalidPassword(Exception):
        pass
