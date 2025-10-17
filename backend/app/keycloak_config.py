from keycloak import KeycloakAdmin, KeycloakOpenID

keycloak_admin = KeycloakAdmin(
    server_url="http://localhost:8080/",
    username="admin",
    password="dUdjas890J!m!djaSDUdasou@",
    realm_name="RealtimeTraffic",
    client_id="ClientNo01",
    client_secret_key="pbDHzsyKV0nNVh1VzzVRcCnP7R64FX28",
    verify=False)

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    client_id="ClientNo01",
    realm_name="RealtimeTraffic",
    client_secret_key="pbDHzsyKV0nNVh1VzzVRcCnP7R64FX28"
)