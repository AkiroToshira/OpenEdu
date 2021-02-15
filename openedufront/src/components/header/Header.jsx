import './header.css'
import {NavLink} from "react-router-dom";
import {useDispatch, useSelector} from "react-redux";
import {logout} from "../../actions/auth";
import {fetchProfile, profileLogout} from "../../actions/profile";
import {newsLogout} from "../../actions/news";

function Header() {
  const dispatch = useDispatch()
  const role = useSelector(state => state.profile)

  const handleLogout = () => {
	dispatch(profileLogout())
	dispatch(newsLogout())
	dispatch(logout())
  }

  if (!role.loading) {
	return (
		<>
		  <nav className="main-header">
			<div className="logo"><NavLink to={"/"}>OpenEdu</NavLink></div>
			<ul className="nav-links-list">
			  {role.perm === 'Teacher' ?
				  <li className="nav-link"><NavLink to={'/teacher/classest'}>Предмети</NavLink></li> :
				  <li className="nav-link"><NavLink to={'/student/classes'}>Предмети</NavLink></li>}
			  {role.perm === 'Student' ? <li><NavLink to={'/tests'}>Тести</NavLink></li> : ''}
			  <li className="nav-link"><NavLink to={'/schedule'}>Розклад</NavLink></li>
			  <li className="nav-link"><NavLink to={'/'}>Новини</NavLink></li>
			</ul>
			<div className="wrapper-buttons">
			  <div className="btn btn-who-logged"><NavLink to={'/profile'}>Профіль</NavLink></div>
			  <div className="btn btn-logged-out"><NavLink to={'/login'} onClick={handleLogout}>logout</NavLink></div>
			</div>
		  </nav>
		</>
	);
  } else {
	return <div></div>
  }
}

export default Header;