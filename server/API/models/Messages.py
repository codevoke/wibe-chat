# models/messages.py
from __future__ import annotations
from enum import Enum

from .db import db, BaseModel


class MessageModel(BaseModel):
    __tablename__ = "messages"

    id = db.Column(db.String, primary_key=True)
    chat_id = db.Column(db.String, db.ForeignKey('chats.id'), nullable=False)
    sender_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    message_type = db.Column(db.Enum(MessageType), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


class MessageType(Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    FILE = "file"