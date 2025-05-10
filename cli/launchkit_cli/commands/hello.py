import typer

app = typer.Typer(help="Example commands")

@app.command()
def world():
    """
    Prints 'Hello, LaunchKit!'
    """

    typer.echo("Hello, LaunchKit!")