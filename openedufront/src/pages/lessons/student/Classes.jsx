import '../classes.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from 'react'
import {BrowserRouter as Router, Switch, Route, useHistory,} from "react-router-dom";


import {fetchLessonsStudent} from "../../../actions/lessonsStudent";
import {fetchLessonsStudentDetailed} from "../../../actions/lessonsStudentByid";
import {fetchDeadlines} from "../../../actions/deadlines";
import {fetchLessonsTeacher} from "../../../actions/lessonsTeacher";

function ClassesStudent() {
  const history = useHistory()
  const dispatch = useDispatch();
  const studentLessons = useSelector(state => state.lessonsStudent)
  const studentLessonsById = useSelector(state => state.lessonsStudentById)
  const state = useSelector(state => state.lessonsTeacher)

  const deadlines = useSelector(state => state.deadlines)

  useEffect(() => {
	dispatch(fetchDeadlines())
  }, [])

  const handleLessonClick = (id) => {
	dispatch(fetchLessonsStudentDetailed(id))
	  localStorage.setItem("lessonId", JSON.stringify(id))
	  history.push("/student/class");
  }

  useEffect(() => {
    console.log(studentLessons.loading)
  }, [studentLessons.loading])

  if (!studentLessons.loading) {
	return (<>
	  <div className="main-container">
		<div className="subject-title"><span>Предмети</span></div>
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
	  </div>

	  {
		!deadlines.loading &&
		<>
		  <div className="subject-title"><span>Дедлайни</span></div>

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
			  {deadlines.deadlines.map(el => {
			    return (
					<tr key={el.id}>

					  <td>{el.name}</td>
					  <td>{el.type}</td>
					  <td>{el.deadline_time}</td>
					  <td>{el.description}</td>
					</tr>
				)
			  })}

			  {/*{% endfor %}*/}
			  </tbody>
			</table>
		  </div>
		</>
	  }

	</>)
  } else {
	return <>
	  <div>Loading...</div>
	</>
  }


}


export default ClassesStudent;