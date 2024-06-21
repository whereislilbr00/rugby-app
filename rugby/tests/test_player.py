from rugby.models.player import Player
from rugby.database import SessionLocal, engine
from rugby.utils import create_player

def test_create_player():
    player_name = "John Doe"
    team_id = 1
    db = SessionLocal()
    player = create_player(db=db, name=player_name, team_id=team_id)
    assert player.name == player_name
    assert player.team_id == team_id
