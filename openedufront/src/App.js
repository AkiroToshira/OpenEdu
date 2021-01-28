import {Component, useEffect} from 'react'

import Header from "./components/header/Header";
import NewsPage from "./pages/news/NewsPage"
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Login from "./pages/login/Login";
import Profile from "./pages/profile/Profile";
import Schedule from "./pages/schedule/Schedule";
import Classest from "./lessons/teacher/Classest";
import Editchapter from "./lessons/teacher/Editchapter";
import Editdeadlines from "./lessons/teacher/Editdeadlines";
import Lessont from "./lessons/teacher/Lessont";
import ClassStudent from "./lessons/student/Class";
import ClassesStudent from "./lessons/student/Classes";


function App() {

//    useEffect(async () => {
//        const data = fetch('http://127.0.0.1:8000/news/')
//        console.log(data)
//    }, [])

  return (
	  <div className="App">
		<Router>
		  <Header/>
		  <Switch>
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

		  </Switch>
		</Router>
	  </div>
  );
}

export default App;
