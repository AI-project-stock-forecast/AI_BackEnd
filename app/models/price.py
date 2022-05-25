from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

from app.db.mysql_connect import Base


class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer, nullable=False, autoincrement=True, primay_key=True)
    event_code = Column(String, ForeignKey("event.code"), nullable=False)
    date = Column(String, nullable=False)
    average = Column(String, nullable=False)


event = relationship("Event", back_populates="price")
