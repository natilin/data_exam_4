from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from sqlalchemy.orm import relationship
from config.base import Base



class Industry(Base):
    __tablename__ = "industry"
    industry_id = Column(Integer, primary_key=True, autoincrement=True)
    industry_name = Column(String(255), unique=True, nullable=False)
    missions = relationship("Mission", back_populates="industry")
