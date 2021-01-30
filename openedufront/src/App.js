import {useEffect} from 'react'

import {Switch, Route} from "react-router-dom";


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
import {Context} from './context'
import useFetch from "./use/useFetch";

const url = "http://127.0.0.1:8000"

function App() {
  const [news, newsLoading] = useFetch(`${url}/news/`)
  const [user, userLoading] = useFetch(`${url}/user/react-info/`)
  // const [profile, profileLoading] = useFetch(`${url}/user/1`)
  useEffect(() => {
	console.log(user)
  }, [userLoading])

  const contextData = {
	news, newsLoading,
  }

  return (
	  <Context.Provider value={contextData}>
		<div className="App">
		  <Header/>
		  <Switch>
			<Route path='/news'>
			  <NewsPage/>
			</Route>
			<Route path='/'>
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

		  </Switch>
		</div>
	  </Context.Provider>
  );

}

export default App;
