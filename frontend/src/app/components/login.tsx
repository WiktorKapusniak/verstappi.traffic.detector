import { useState } from "react";
import axios from "axios";
export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  async function getData(): Promise<void> {
    const data = {
      username: username,
      password: password
    }
    const login_post = axios.post("http://127.0.0.1:5000/login", data).then((res) => {
      if(res.status==200){
        alert("login ok")
      }
    }).catch(()=>{
      alert("login failed")
    }) // POST do backendu z loginem i haslem uzytkownika, bez szyfrowania
  }

  return (
    <main>
      <form onSubmit={(e) => {
        e.preventDefault()
        getData()}}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Your username"/>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Your password"/>
        <button type="submit">Send</button>
      </form>
    </main>
  );
}
