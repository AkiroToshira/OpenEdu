import './login.css'
import {FaUserAlt} from 'react-icons/fa';
import {RiLockPasswordFill} from 'react-icons/ri';

import {useState} from 'react'
import axios from "axios";
import { useHistory } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  let history = useHistory();

  const handleSubmit = (e) => {
	axios.post("http://127.0.0.1:8000/token/", {
	  password,
	  username
	}).then(res => {
	  localStorage.setItem('user', JSON.stringify(res.data))
	  if (res.status === 200) {
		history.push("/news");
	  }
	}).catch(e => {
	  if(e.response) {
		setError(e.response.data.detail)
	  }
	})
	e.preventDefault();
  }

  return (
	  <div className="login">
		<div className="skew-block"/>
		<div className="skew-block-bottom"/>
		<form className="login-form" onSubmit={handleSubmit}>
		  <h1 className="login-title">Вітаємо на OpenEdu</h1>
		  <div className="icon-wrapper">
			<input type="text" id="user" name="user" placeholder="username"
				   onChange={(e) => setUsername(e.target.value)}/>
			<FaUserAlt/>
		  </div>
		  <div className="icon-wrapper">
			<input type="text" id="password" name="password" placeholder="password"
				   onChange={(e) => setPassword(e.target.value)}/>
			<RiLockPasswordFill/>
		  </div>
		  {error}
		  <input type="submit" className="login-submit" value="Submit"/>

		</form>
	  </div>
  );
}

export default Login;
