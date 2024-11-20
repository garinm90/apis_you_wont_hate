import typer

from app.database import create_db_and_tables
from app.factories import UserFactory

app = typer.Typer(no_args_is_help=True)


@app.command(help='Generates database fixtures')
def seed_database():
    UserFactory.create_batch(50)

@app.command(help='Create database and tables if it does not already exists')
def create_database():
    create_db_and_tables()


@app.callback()
def callback():
    pass


def main():
    app()
