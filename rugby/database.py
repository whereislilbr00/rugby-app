from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./rugby.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    # Import models here to ensure they are registered with SQLAlchemy
    from rugby.models.player import Player
    from rugby.models.team import Team
    from rugby.models.match import Match

    Base.metadata.create_all(bind=engine)
