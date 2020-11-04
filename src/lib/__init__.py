"""Third party modules"""
from keycloak import KeycloakAdmin


def configure_keycloak_admin():
    """Configure keycloak admin client"""

    keycloak_admin = KeycloakAdmin(
        server_url="http://localhost:8080/auth/",
        username="admin",
        password="password",
        realm_name="master",
        verify=False,
    )

    return keycloak_admin
