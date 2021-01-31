import {BrowserRouter as Router, Switch, Route, useHistory} from "react-router-dom";
import {Context} from './context'

import Header from "./components/header/Header";
import NewsPage from "./pages/news/NewsPage"
import Login from "./pages/login/Login";
import Profile from "./pages/profile/Profile";
import Schedule from "./pages/schedule/Schedule";
import Classest from "./pages/lessons/teacher/Classest";
import Editchapter from "./pages/lessons/teacher/Editchapter";
import Editdeadlines from "./pages/lessons/teacher/Editdeadlines";
import Lessont from "./pages/lessons/teacher/Lessont";
import ClassStudent from "./pages/lessons/student/Class";
import ClassesStudent from "./pages/lessons/student/Classes";

import {useState, useEffect, useReducer} from "react";
import axios from "axios";

//ПЕРЕПИСАТИ КОД І РОЗКЛАСТИ ПО ПАПКАМ
function newsReducer(state = [], action) {
  switch (action.type) {
	case 'ADD':
	  return [...state, action.payload]
	default:
	  return state;
  }
}

const userInitialState = {
  password: "",
  username: "",
  isLogged: false,
  id: 0,
  role: 'student',
  refresh: '',
  access: '',
}

function userReducer(state = userInitialState, action) {
  switch (action.type) {
	case 'LOGIN':
	  return {...state, ...action.payload}
	case "SAVE":
	  console.log(action.payload)
	  localStorage.setItem('user', JSON.stringify({...state, ...action.payload}))
	  return {...state, ...action.payload}
	case 'LOGOUT':
	  return {...state, ...action.payload}
	default:
	  return state;
  }
}

const checkIfUserLogged = () => !!JSON.parse(localStorage.getItem('user'));


function App() {
  const history = useHistory()
  const [loading, setLoading] = useState(localStorage.getItem('user') === null)
  const userInfo = JSON.parse(localStorage.getItem('user'));
  const [state, dispatch] = useReducer(userReducer, {...userInitialState, isLogged: checkIfUserLogged(), ...userInfo})

  useEffect(() => {
	console.log(state)
  }, [state])

  const handleLogin = (isLogged) => {
	if (isLogged) {
	  // history.push('/')
	  return (<Switch>
		<Route exact path='/'>
		  <NewsPage/>
		</Route>
		<Route path='/login'>
		  <Login/>
		</Route>
		<Route path='/profile'>
		  <Profile/>
		</Route>
		<Route path='/schedule'>
		  <Schedule/>
		</Route>
		{/*TEACHER*/}
		<Route path='/teacher/classest'>
		  <Classest/>
		</Route>
		<Route path='/teacher/editchapter'>
		  <Editchapter/>
		</Route>
		<Route path='/teacher/editdeadlines'>
		  <Editdeadlines/>
		</Route>
		<Route path='/teacher/lessont'>
		  <Lessont/>
		</Route>
		{/*STUDENT*/}
		<Route path='/student/class'>
		  <ClassStudent/>
		</Route>
		<Route path='/student/classes'>
		  <ClassesStudent/>
		</Route>

		<Route path='*'>
		  <div>No page found</div>
		</Route>
	  </Switch>)
	} else {
	  return <Login/>
	}
  }


  return (
	  <Context.Provider value={[state, dispatch]}>
		<Router>
		  <div className="App">
			{state.isLogged ? <Header/> : ''}
			{handleLogin(state.isLogged)}
		  </div>
		</Router>
	  </Context.Provider>
  );

}

export default App;
