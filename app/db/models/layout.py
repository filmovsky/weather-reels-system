from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base


class Layout(Base):
    __tablename__ = "layouts"

    id = Column(Integer, primary_key=True, index=True)

    layout_id = Column(String, unique=True, index=True)

    type = Column(String)

    style = Column(String)

    active = Column(Boolean, default=True)