import {useRouter} from "next/navigation"
import {keycloak} from "../keycloak";
import LoggedUser from "./loggedUser";

export default function Main() {
    const router = useRouter();
    return (
    <main>
      <div>Don&apos;t honk in the woods</div>
      {!keycloak.authenticated ? 
        (<button onClick={() => keycloak.login()}>Zaloguj się</button>) : 
        (<LoggedUser></LoggedUser>)}
    </main>
  );
}
