import click
from sqlalchemy.orm import sessionmaker
from rugby.database import engine, SessionLocal, init_db
from rugby.models.player import Player

# Initialize the database
init_db()

Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Player name')
def add_player(name):
    """Add a new player to the database."""
    player = Player(name=name)
    session.add(player)
    session.commit()
    click.echo(f'Player {name} added.')

@cli.command()
def list_players():
    """List all players in the database."""
    players = session.query(Player).all()
    for player in players:
        click.echo(f'{player.id}: {player.name}')

if __name__ == '__main__':
    cli()
