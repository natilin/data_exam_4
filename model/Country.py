from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config.base import Base


class Country(Base):
    __tablename__ = "country"
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), nullable=False, unique=True)
    cities = relationship("City", back_populates="country")