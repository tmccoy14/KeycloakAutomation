"""Standard library"""
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin

# CONFIGURE CLIENT
keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/auth/",
    client_id="example_client",
    realm_name="example_realm",
    client_secret_key="secret",
)

# KEYCLOAK ADMIN
keycloak_admin = KeycloakAdmin(
    server_url="http://localhost:8080/auth/",
    username="example-admin",
    password="secret",
    realm_name="example_realm",
    client_secret_key="client-secret",
    verify=True,
)
