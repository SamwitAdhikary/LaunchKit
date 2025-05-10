import typer

app = typer.Typer(help="Authenticate with LaunchKit backend")

@app.command()
def login(
    email: str = typer.Option(..., prompt=True, help="Your user email"),
    password: str = typer.Option(..., prompt=True, hide_input=True, help="Your password"),
):
    """
    Login via email and password (stub).
    """

    typer.echo(f"[stub] Logging in {email}")