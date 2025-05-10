import typer

app = typer.Typer(help="Rollback deployments")

@app.command()
def rollback(version: str = typer.Argument(..., help="Version to roll back to")):
    """
    Roll back to a previous version (stub).
    """
    typer.echo(f"[stub] Rolling back to {version}")
