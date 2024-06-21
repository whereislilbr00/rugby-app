from sqlalchemy import Column, Integer, String, ForeignKey
from rugby.database import Base

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    result = Column(String)
