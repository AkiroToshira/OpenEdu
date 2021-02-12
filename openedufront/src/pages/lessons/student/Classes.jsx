import '../classes.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from 'react'
import {BrowserRouter as Router, Switch, Route, useHistory,} from "react-router-dom";


import {fetchLessonsStudent} from "../../../actions/lessonsStudent";
import {fetchLessonsStudentDetailed} from "../../../actions/lessonsStudentByid";

function ClassesStudent() {
  const history = useHistory()
  const dispatch = useDispatch();
  const studentLessons = useSelector(state => state.lessonsStudent)

  useEffect(() => {
	dispatch(fetchLessonsStudent())
  }, [])

  const handleLessonClick = (id) => {
	dispatch(fetchLessonsStudentDetailed(id))
	history.push("/student/class");
  }

  if(!studentLessons.loading) {
	return (
		<div className="main-container">
		  <div className="subjet-title"><span>Предмети</span></div>
		  <div className="inner-container">
			{studentLessons.lessons.map((el, i) => {
			  return <a href="#" className="col2" key={el.lesson.id} onClick={() => handleLessonClick(el.lesson.id)}>
				<div className="inner-information">
				  <span>{el.lesson.name}</span>
				  <span>Teacher</span>
				</div>
			  </a>
			})}

		  </div>

		  <div className="subjet-title"><span>Дедлайни</span></div>

		  <div className="deadline-container">
			<table className="content-table">
			  <thead>
			  <tr>
				<th>Назва предмату</th>
				<th>Назва задачі</th>
				<th>Дедлайн</th>
				<th>Додатковий опис</th>
			  </tr>
			  </thead>
			  <tbody>
			  {/*{% for x in get_deadlines %}*/}
			  <tr>

				<td>kl;</td>
				<td>kl;</td>
				<td>kl;k</td>
				<td>--</td>
			  </tr>
			  <tr>

				<td>kl;</td>
				<td>kl;</td>
				<td>kl;k</td>
				<td>--</td>
			  </tr>
			  <tr>

				<td>kl;</td>
				<td>kl;</td>
				<td>kl;k</td>
				<td>--</td>
			  </tr>
			  {/*{% endfor %}*/}
			  </tbody>
			</table>
		  </div>
		</div>
	);
  } else {
    return <>
		<div>Loading...</div>
	</>
  }
}


export default ClassesStudent;