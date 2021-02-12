import './login.css'
import {FaUserAlt} from 'react-icons/fa';
import {RiLockPasswordFill} from 'react-icons/ri';

import {useState} from 'react'
import {useHistory} from "react-router-dom";


import {useDispatch, useSelector} from "react-redux";
import {login} from "../../actions/auth";

import {motion} from 'framer-motion'

const modal = {
  hidden: {
	y: "-100vh",
	opacity: 0,
  },
  visible: {
	y: "200px",
	opacity: 1,
	transition: {delay: 0.5}
  }
}

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
  const variants = {
	hidden: { opacity: 0 },
	visible: { opacity: 1 },
  }
  return (
	  <div className="login">
		<motion.div className="error-pop-up" variants={modal}>
		  {error}
		</motion.div>

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
