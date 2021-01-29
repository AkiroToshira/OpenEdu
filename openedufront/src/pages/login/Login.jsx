import './login.css'
import {FaUserAlt} from 'react-icons/fa';
import {RiLockPasswordFill} from 'react-icons/ri';
import {useState} from "react";

function Login() {
  return (
	  <div className="login">
		<div className="skew-block"></div>
		<div className="skew-block-bottom"></div>
		<form className="login-form">
		  <h1 className="login-title">Вітаємо на OpenEdu</h1>
		  <div className="icon-wrapper">
			<input type="text" id="user" name="user" placeholder="username"/>
			<FaUserAlt/>
		  </div>
		  <div className="icon-wrapper">
			<input type="text" id="password" name="password" placeholder="password"/>
			<RiLockPasswordFill/>
		  </div>

		  <input type="submit" className="login-submit" value="Submit"/>

		</form>
	  </div>
  );
}

export default Login;
