from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base


class AudioAsset(Base):
    __tablename__ = "audio_assets"

    id = Column(Integer, primary_key=True, index=True)

    region_id = Column(String, index=True)

    language = Column(String)

    voice_id = Column(String)

    file_path = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)