from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from rugby.database import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team", back_populates="players")
