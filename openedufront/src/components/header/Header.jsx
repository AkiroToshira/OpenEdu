import './header.css'
import {NavLink} from "react-router-dom";

function Header() {
  return (
	  <>
		<nav className="main-header">
		  <div className="logo"><NavLink to={"/news"}>OpenEdu</NavLink></div>
		  <ul className="nav-links-list">
			<li className="nav-link"><NavLink to={'/subject'}>Предмети</NavLink></li>
			<li className="nav-link"><NavLink to={'/schedule'}>Розклад</NavLink></li>
			<li className="nav-link"><NavLink to={'/news'}>Новини</NavLink></li>
		  </ul>
		  <div className="wrapper-buttons">
			<div className="btn btn-who-logged"><NavLink to={'/profile'}>Student</NavLink></div>
			<div className="btn btn-logged-out"><NavLink to={'/'}>logout</NavLink></div>
		  </div>
		</nav>
	  </>
  );
}

export default Header;