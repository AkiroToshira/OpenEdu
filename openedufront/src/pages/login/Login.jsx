import './login.css'
import {FaUserAlt} from 'react-icons/fa';
import {RiLockPasswordFill} from 'react-icons/ri';

import {useState} from 'react'
import axios from "axios";
import {useHistory} from "react-router-dom";
import {useContext, useEffect} from "react";
import {Context} from "../../context";
import useFetch from "../../use/useFetch";

function Login() {
  const [state, dispatch] = useContext(Context);
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  let history = useHistory();

  //ПЕРЕПИСАТИ НА ХУК
  useEffect(async () => {
	if (JSON.parse(localStorage.getItem('user'))) {
	  const jwt = JSON.parse(localStorage.getItem('user'))
	  axios.get("http://127.0.0.1:8000/user/react-info/", {
		headers: {
		  "Authorization": 'JWT ' + jwt.access,
		}
	  }).then(res => {
	    console.log(res)
		dispatch({type: "SAVE", payload: {...jwt, id: res.data.id, role: res.data.perm}})
		dispatch({type: 'LOGIN', payload: {id: res.data.id, role: res.data.perm}})
	  }).catch(e => {
	    console.log('помилка', e)
	  })
	}
  }, [])

  const handleSubmit = (e) => {
	axios.post("http://127.0.0.1:8000/token/", {
	  password,
	  username
	}).then(res => {
	  if (res.status === 200) {
		dispatch({type: "SAVE", payload: {...res.data, username, password, isLogged: true}})
		dispatch({type: 'LOGIN', payload: {username, password, isLogged: true}})
		history.push("/");
	  }
	}).catch(e => {
	  if (e.response) {
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
			<input type="password" id="password" name="password" placeholder="password"
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
