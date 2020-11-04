"""Standard library"""
import csv
import time

"""Third party modules"""
import click
import keycloak
import click_spinner

"""Internal application modules"""
from src.main import pass_environment
from src.lib import configure_keycloak_admin


@click.group("create", short_help="Create Keycloak realms and clients.")
@pass_environment
def cli(ctx):
    """Keycloak create realm and client."""


@cli.command("realm", short_help="Create Keycloak realm.")
@click.option(
    "--name", "-n", required=True, prompt="Realm name", help="Realm name.",
)
@pass_environment
def realm(ctx, name):
    """Keyclaok create realm and client. Create your Keycloak realm."""

    ctx.log("Creating Keycloak realm...")

    with click_spinner.spinner():
        time.sleep(2)

        # configure key cloak admin client
        keycloak_admin = configure_keycloak_admin()

        # try to create realm if it doesn't already exist
        try:
            new_realm = keycloak_admin.create_realm(
                {"realm": name, "enabled": True,}, skip_exists=False
            )
        except keycloak.exceptions.KeycloakGetError as e:
            ctx.log("Could not create realm", level="error")
            raise click.UsageError("Keycloak realm %s already exists." % name)

    ctx.log("Realm created successfully...")


@cli.command("client", short_help="Create Keycloak client.")
@click.option(
    "--name", "-n", required=True, prompt="Client name", help="Client name.",
)
@click.option(
    "--realm", "-r", required=True, prompt="Realm name", help="Realm name.",
)
@pass_environment
def client(ctx, name, realm):
    """Keyclaok create realm and client. Create your Keycloak client."""

    ctx.log("Creating Keycloak client...")

    with click_spinner.spinner():
        time.sleep(2)

        # configure key cloak admin client
        keycloak_admin = configure_keycloak_admin()

        # set keycloak realm
        keycloak_admin.realm_name = realm

        # get list of realms
        list_realms = keycloak_admin.get_realms()

        # ensure realm specified exists before creating client within realm
        for realm_obj in list_realms:
            if realm == realm_obj["realm"]:
                create_client = keycloak_admin.create_client(
                    {"clientId": name, "enabled": True}
                )

    ctx.log("Client created successfully...")
