import typer

app = typer.Typer(help="Configuration management")

@app.command("set")
def set_config(key: str = typer.Argument(...), value: str = typer.Argument(...)):
    """
    Set a configuration key (stub).
    """
    typer.echo(f"[stub] Setting {key} = {value}")
