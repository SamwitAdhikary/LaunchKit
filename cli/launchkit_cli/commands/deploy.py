import typer

app = typer.Typer(help="Deploy an application")

@app.command()
def deploy():
    """
    Deploy the current project (stub).
    """
    typer.echo("[stub] Deploying application…")
