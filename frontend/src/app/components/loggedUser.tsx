import {keycloak} from "../keycloak";
export default function LoggedUser() {
    return (
    <main>
      <div>Gratuluje jestes zalogowany</div>
      <button onClick={() => keycloak.logout()}>Wyloguj się</button>
    </main>
  );
}
