import typer
from .commands import (
    hello,
    login,
    init as init_cmd,
    deploy,
    env,
    domain,
    config,
    rollback,
)

app = typer.Typer(help="LaunchKit CLI - deploy and manage apps on AWS")

# Register sub-commands
app.add_typer(hello.app, name="hello")
app.add_typer(login.app, name="login")
app.add_typer(init_cmd.app, name="init")
app.add_typer(deploy.app, name="deploy")
app.add_typer(env.app, name="env")
app.add_typer(domain.app, name="domain")
app.add_typer(config.app, name="config")
app.add_typer(rollback.app, name="rollback")