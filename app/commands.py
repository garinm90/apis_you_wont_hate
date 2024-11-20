import typer

from app.factories import UserFactory

app = typer.Typer(no_args_is_help=True)


@app.command(help='Generates database fixtures')
def seed_database():
    UserFactory.create_batch(50)


@app.callback()
def callback():
    pass


def main():
    app()
