from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base


class ScriptAsset(Base):
    __tablename__ = "script_assets"

    id = Column(Integer, primary_key=True, index=True)

    region_id = Column(String, index=True)

    language = Column(String)

    content = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)