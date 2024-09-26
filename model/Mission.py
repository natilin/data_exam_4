from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config.base import Base


class Mission(Base):
    __tablename__ = "mission"
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    position_id = Column(Integer, ForeignKey("position.position_id"))
    position = relationship("Position", back_populates="missions", lazy="joined" )
    industry_id = Column(Integer, ForeignKey("industry.industry_id"))
    industry = relationship("Industry", back_populates="missions", lazy="joined")

    target_priority = Column(String(100))
    target_type = Column(String(255))


