import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rugby.database import Base, init_db
from rugby.models.player import Player

# Setup a temporary database for testing
@pytest.fixture(scope='module')
def test_session():
    # Create an in-memory SQLite database
    engine = create_engine('sqlite:///:memory:')
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

def test_add_player(test_session):
    player = Player(name="Test Player")
    test_session.add(player)
    test_session.commit()
    assert test_session.query(Player).count() == 1

def test_list_players(test_session):
    players = test_session.query(Player).all()
    assert len(players) == 1
    assert players[0].name == "Test Player"
