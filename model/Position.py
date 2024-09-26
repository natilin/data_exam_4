from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from sqlalchemy.orm import relationship
from config.base import Base


class Position(Base):
    __tablename__ = "position"
    position_id = Column(Integer, primary_key=True, autoincrement=True, )
    target_longitude = Column(Numeric(10, 6))
    target_latitude = Column(Numeric(10, 6))
    target_id = Column(String(100), unique=True)
    city_id = Column(Integer, ForeignKey("city.city_id"))
    city = relationship("City", back_populates="positions", lazy="joined")

    missions = relationship("Mission", back_populates="position", lazy="joined")
