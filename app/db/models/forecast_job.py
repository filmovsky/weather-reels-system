from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime


class ForecastJob(Base):
    __tablename__ = "forecast_jobs"

    id = Column(Integer, primary_key=True, index=True)

    region_id = Column(String, index=True)

    forecast_type = Column(String)

    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)