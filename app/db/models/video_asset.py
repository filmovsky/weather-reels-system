from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base


class VideoAsset(Base):
    __tablename__ = "video_assets"

    id = Column(Integer, primary_key=True, index=True)

    region_id = Column(String, index=True)

    file_path = Column(String)

    layout_id = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)