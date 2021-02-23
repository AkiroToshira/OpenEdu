import '../classes.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect, useState} from 'react'
import {BrowserRouter as Router, Switch, Route, useHistory,} from "react-router-dom";


import {fetchLessonsStudentDetailed} from "../../../actions/lessonsStudentByid";
import {fetchDeadlines} from "../../../actions/deadlines";

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


  const handleTesting = (id) => {
	localStorage.setItem("test-lesson-id", JSON.stringify(id))
	history.push("/tests");
  }


  if (!studentLessons.loading) {
	return (<>
	  <div className="main-container">
		<div className="subject-title"><span>Предмети</span></div>
		<div className="inner-container">
		  {studentLessons.lessons.map((el, i) => {
			return <a className="col2" key={el.lesson.id} >
			  <div className="inner-information" onClick={() => handleLessonClick(el.lesson.id)}>
				<span>{el.lesson.name}</span>
				<span>Teacher</span>
			  </div>
			  <div className={"do-testing"} onClick={() => handleTesting(el.lesson.id)}>
        <i class="fas fa-poll-h"></i>
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
			  <tr className="teacher_header">
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
					<tr key={el.id} className="tr-info">

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
