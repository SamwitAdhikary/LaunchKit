import typer
from launchkit_cli.services.auth import AuthService

app = typer.Typer(help="Authenticate with LaunchKit backend", invoke_without_command=True)

@app.callback(invoke_without_command=True)
def login(
    email: str = typer.Option(..., prompt=True, help="Your user email"),
    password: str = typer.Option(..., prompt=True, hide_input=True, help="Your password"),
    api_url: str = typer.Option(
        None,
        "--api-url",
        envvar="LAUNCHKIT_API_URL",
        help="The base URL of the LaunchKit API (e.g. http://localhost:8000/api/v1)",
    ),
):
    """
    Login via email and password. Stores the access token in your system keyring.
    """
    api_url = api_url or "http://localhost:8000/api/v1"
    service = AuthService(api_url)
    try:
        token = service.login(email, password)
        typer.secho("Login successful!", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Login failed: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)