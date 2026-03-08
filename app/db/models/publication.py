from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base


class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)

    region_id = Column(String, index=True)

    platform = Column(String)

    video_path = Column(String)

    status = Column(String, default="pending")

    published_at = Column(DateTime, default=datetime.utcnow)