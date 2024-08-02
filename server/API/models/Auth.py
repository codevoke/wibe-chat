# models/auth.py
from .db import db, BaseModel
from passlib.hash import pbkdf2_sha256


class AuthModel(BaseModel):
    __tablename__ = "auth"

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    hashed_password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @classmethod
    def verify_password(cls, user_id, password):
        auth = cls.query.filter_by(user_id=user_id).first()
        if auth and pbkdf2_sha256.verify(password, auth.hashed_password):
            return True
        return False

    @classmethod
    def create_hashed_password(cls, password):
        return pbkdf2_sha256.hash(password)
