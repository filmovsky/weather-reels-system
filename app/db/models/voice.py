from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base


class Voice(Base):
    __tablename__ = "voices"

    id = Column(Integer, primary_key=True, index=True)

    voice_id = Column(String, unique=True, index=True)

    language = Column(String)

    gender = Column(String)

    style = Column(String)

    energy = Column(String)

    active = Column(Boolean, default=True)