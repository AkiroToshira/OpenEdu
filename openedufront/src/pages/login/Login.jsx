import './login.css'
import {FaUserAlt} from 'react-icons/fa';
import {RiLockPasswordFill} from 'react-icons/ri';

import {useState} from 'react'
import {useHistory} from "react-router-dom";


import {useDispatch, useSelector} from "react-redux";
import {login} from "../../actions/auth";



function Login() {
  const dispatch = useDispatch()
  const history = useHistory()
  const error = useSelector(state => state.message.message)

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')


  const handleSubmit = (e) => {
	if (username && password) {
	  dispatch(login(username, password))
		  .then(() => {
			history.push("/");
			window.location.reload();
		  })
	} else {
	  alert('oops')
	}
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
		  <input type="submit" className="login-submit" value="Submit"/>

		</form>
	  </div>
  );
}

export default Login;
