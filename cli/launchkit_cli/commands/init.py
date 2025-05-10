import typer

app = typer.Typer(help="Initialize a new LaunchKit project")

@app.command()
def init(
    project_name: str = typer.Argument(..., help="Name of your project"),
):
    """
    Generate launchkit.json (stub).
    """
    typer.echo(f"[stub] Initializing project '{project_name}'")
