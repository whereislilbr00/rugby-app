from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from rugby.database import Base

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    players = relationship("Player", back_populates="team")
