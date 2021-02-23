import '../student_grades/grade.css'
import './teacher_grades.css'
import {useQuery} from "react-query";
import {useState, useEffect} from 'react'
import axios from "axios";
import {useDispatch, useSelector} from "react-redux";
import {fetchGradesLessons, fetchTeacherGradesLessons, updateGrade} from "../../actions/displayGradesLessons";


export default function TeacherGrades() {
  const state = useSelector(state => state)
  const dispatch = useDispatch()
  const [show, setShow] = useState(false)


  useEffect(() => {
	if (state.gradesLessons.lessons.length < 1) {
	  dispatch(fetchGradesLessons())
	}

  }, [state.gradesLessons.lessons])


  const handleFetchingData = async (id) => {
    setShow(p => !p)
    dispatch(fetchTeacherGradesLessons(id))
  }

  const changeGradeValue = async (id, col) => {
	let value = prompt("value: ")
	dispatch(updateGrade(id, value, col))
  }

  if(state.gradesLessons.loading) {
    return <div>Loading...</div>
  }

  if (!state.gradesLessons.loading) {
	return <div className="main-container">
	  <div className="subject-title"><span>Оцінки по предметам:</span></div>
	  <div className="inner-container">
		{!state.gradesLessons.loading && state.gradesLessons.lessons.map((el, i) => {
		  return <a className="col2" onClick={() => handleFetchingData(el.id)}>
			<div className="inner-information">
			  <span>{el.lesson.name}</span>
			  <a href={`http://127.0.0.1:5000/simple/${el.id}`} style={{"marginTop": "10px"}} target={"_blank"}>звіт</a>
			</div>
		  </a>
		})}
	  </div>
	  {!state.teacherGrades.loading &&
	  <div className="teacher_grades_table" style={{'display': `${show ? 'block' : 'none'}`}}
		   class="gradebook_container">
		<div className="grade_element">
		  <table>
			<thead>
			<tr>
			  {state.teacherGrades && <th>{state.teacherGrades.group.group.name}</th>}
			  {state.teacherGrades && state.teacherGrades.columns.map((el, i) => {
				return <th key={i}>{el.date}</th>
			  })}
			</tr>
			</thead>
			<tbody>
			{state.teacherGrades && [...new Array(state.teacherGrades.columns[0].grades.length)].map((item, i) => {
			  return <tr>
				<td>{state.teacherGrades.columns[0].grades[i].user.first_name} {state.teacherGrades.columns[0].grades[i].user.middle_name}</td>
				{state.teacherGrades && state.teacherGrades.columns.map((element, grade_index) => {
				  return <td
					  onClick={() => changeGradeValue(state.teacherGrades.columns[grade_index].grades[i].id,grade_index)}>{state.teacherGrades.columns[grade_index].grades[i].value}</td>
				})}
			  </tr>
			})}
			</tbody>
		  </table>
		</div>
	  </div>}

	</div>
  }
}
