# models/attachments.py
from enum import Enum

from .db import db, BaseModel


class AttachmentModel(BaseModel):
    __tablename__ = "attachments"

    id = db.Column(db.String, primary_key=True)
    message_id = db.Column(db.String, db.ForeignKey('messages.id'), nullable=False)
    file_url = db.Column(db.String, nullable=False)
    file_type = db.Column(db.String(20), nullable=False)  # "image", "video", "document"
    uploaded_at = db.Column(db.DateTime, nullable=False)


class FileType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "DOCUMENT"
