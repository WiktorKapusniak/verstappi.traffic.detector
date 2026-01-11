import Keycloak from "keycloak-js";

export const keycloak = new Keycloak({
  url: "https://verstappi.pl:31514/keycloak",
  realm: "RealtimeTraffic",
  clientId: "VerstappiClient",
});
