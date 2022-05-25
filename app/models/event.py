from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from app.db.mysql_connect import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, nullable=False, autoincrement=True, primay_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)


prices = relationship("Price", back_populates="event")
