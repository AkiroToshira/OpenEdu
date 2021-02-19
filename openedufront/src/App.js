import {BrowserRouter as Router, Switch, Route, useHistory,} from "react-router-dom";

import Header from "./components/header/Header";
import NewsPage from "./pages/news/NewsPage"
import Login from "./pages/login/Login";
import Schedule from "./pages/schedule/Schedule";
import Classest from "./pages/lessons/teacher/Classest";
import Editchapter from "./pages/lessons/teacher/Editchapter";
import Editdeadlines from "./pages/lessons/teacher/Editdeadlines";
import Lessont from "./pages/lessons/teacher/Lessont";
import ClassStudent from "./pages/lessons/student/Class";
import ClassesStudent from "./pages/lessons/student/Classes";


import {useDispatch, useSelector} from "react-redux";
import Profile from "./pages/profile/Profile";
import {useEffect} from "react";
import {fetchProfile} from "./actions/profile";
import {fetchLessonsTeacher} from "./actions/lessonsTeacher";
import {fetchLessonsStudent} from "./actions/lessonsStudent";
import {fetchSchedule} from "./actions/schedule";
import {fetchNews} from "./actions/news";
import Tests from "./pages/tests/Tests";
import Grades from "./pages/grades/Grades";


function App() {
  const history = useHistory()
  const dispatch = useDispatch()
  const auth = useSelector((state) => state.auth)

  useEffect(() => {
	if (auth.isLoggedIn) {
	  dispatch(fetchNews())
	  dispatch(fetchProfile())
	  dispatch(fetchLessonsTeacher())
	  dispatch(fetchLessonsStudent())
	  dispatch(fetchSchedule())
	}
  }, [])

  if (auth.isLoggedIn) {
	return (<>
	  {auth.isLoggedIn ? <Header/> : ''}
	  <div className="App">
		<Switch>
		  <Route exact path='/'>
			<NewsPage/>
		  </Route>
		  <Route path='/tests'>
			<Tests/>
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
		  {/* ОЦІНКИ */}
		  <Route path='/students-grades'>
			<Grades/>
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
	</>)
  } else {
	history.push('/login')
	return <Login/>
  }
}

export default App;
