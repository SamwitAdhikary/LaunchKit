import typer

app = typer.Typer(help="Manage custom domains")

@app.command("add")
def add_domain(domain: str = typer.Argument(..., help="Domain to add")):
    """
    Add a custom domain (stub).
    """
    typer.echo(f"[stub] Adding domain {domain}")
