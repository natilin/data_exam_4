from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config.base import Base


class City(Base):
    __tablename__ = "city"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), nullable=False,)
    country_id = Column(Integer, ForeignKey("country.country_id"))
    country = relationship("Country", back_populates="cities")

    positions = relationship("Position", back_populates="city")
