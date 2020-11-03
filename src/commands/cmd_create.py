"""Third party modules"""
import click

"""Internal application modules"""
from src.main import pass_environment


@click.group("create", short_help="Create Keycloak realms and clients.")
@pass_environment
def cli(ctx):
    """Keycloak create realm and client."""


@cli.command("realm", short_help="Create Keycloak realm.")
@click.option(
    "--name", "-n", required=True, prompt="Realm name", help="Realm name.",
)
@pass_environment
def realm(ctx, realm):
    """Keyclaok create realm and client. Create your Keycloak realm."""

    print("Hello from the realm")


@cli.command("client", short_help="Create Keycloak client.")
@click.option(
    "--name", "-n", required=True, prompt="Client name", help="Client name.",
)
@pass_environment
def client(ctx, name):
    """Keyclaok create realm and client. Create your Keycloak client."""

    print("Hello from the client")
