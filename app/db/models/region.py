from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.base import Base


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(String, unique=True, index=True)
    name = Column(String)
    country = Column(String)
    language = Column(String)
    timezone = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    priority = Column(Integer)
    active = Column(Boolean, default=True)