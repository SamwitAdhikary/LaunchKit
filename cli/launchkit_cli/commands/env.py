import typer

app = typer.Typer(help="Manage environments")

@app.command("list")
def list_envs():
    """
    List environments (stub).
    """
    typer.echo("[stub] Available environments: dev, staging, production")
