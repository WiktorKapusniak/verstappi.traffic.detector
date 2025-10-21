import Image from "next/image";
import {useRouter} from "next/navigation"

export default function Main() {
    const router = useRouter();
    return (
    <main>
      <div>Don't honk in the woods</div>
      <button type="button" onClick={() => router.push("/login")}>Move to login</button>
    </main>
  );
}
