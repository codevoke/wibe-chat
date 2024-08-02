# models/chats.py
from .db import db, BaseModel


class ChatModel(BaseModel):
    __tablename__ = "chats"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    is_group = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
