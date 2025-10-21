import Image from "next/image";
import { stringify } from "querystring";
import { useState, useEffect } from "react";
//bcrypt todo, hashowanie hasel
export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  async function getData(): Promise<void> {
    const data = {
      username: username,
      password: password
    }
    const login_options = {
      method: "POST",
      headers:{"Content-Type":"application/json"},
      body: JSON.stringify(data)
    }
    console.log(login_options.body)
    const fetcher = fetch("http://127.0.0.1:5000/login", login_options).then(res => res.json()).then(res => console.log(res))
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