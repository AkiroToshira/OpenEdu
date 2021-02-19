import '../student_grades/grade.css'
import './teacher_grades.css'
import {useQuery} from "react-query";
import {useState} from 'react'
import axios from "axios";
import {useSelector} from "react-redux";


export default function TeacherGrades() {
  const state = useSelector(state => state)
  const [getData, setGetData] = useState(null)
  const [show, setShow] = useState(false)
  const [loadingState, setLoadingState] = useState(false)
  const [msg, setMSG] = useState('Loading...')

  const {isLoading, error, data} = useQuery('fetchGradebook', () =>
	  axios(`http://127.0.0.1:8000/gradebook/gradebooklist`, {
		headers: {
		  "Authorization": "JWT " + state.auth.token.access,
		}
	  }))


  const handleFetchingData = async (id) => {
	setMSG('Loading...')
	setGetData(null)
	setLoadingState(true)
	setTimeout(() => {
	  if(loadingState === false) {
		setMSG('немає даних')
	  }
	}, 5000)
	const response = await axios.get(`http://127.0.0.1:8000/gradebook/teacher/${id}`, {
	  headers: {
		"Authorization": "JWT " + state.auth.token.access,
	  }
	})
	if(response.status === 200){
	  setGetData(response.data)
	  setShow(p=>!p)
	  setLoadingState(false)
	}

  }

  const handleExpandClick = (e) => {
	let display = e.target.nextSibling.style.display;
	e.target.nextSibling.style.display = display === 'block' ? 'none' : 'block'
  }


  if (isLoading) {
	return <div>Loading...</div>
  }

  if (!isLoading) {
	return <div className="main-container">
	  <div className="subject-title"><span>Оцінки по предметам:</span></div>
	  <div className="inner-container">
		{data && data.data.map((el, i) => {
		  return <a className="col2" onClick={() => handleFetchingData(el.id)}>
			<div className="inner-information">
			  <span>{el.lesson.name}</span>
			</div>
		  </a>
		})}
	  </div>
	  {loadingState && msg}
	  <div className="teacher_grades_table" style={{'display': `${show ? 'block' : 'none'}`}}>
		<div className="grade_element">
		  <table>
			<tr>
			  {getData !== null && <th>{getData.group.group.name}</th>}
			  {getData && getData.columns.map((el, i) => {
				return <th>{el.date}</th>
			  })}
			</tr>
			{getData && [...new Array(getData.columns[0].grades.length)].map((item, i) => {
			  return <tr>
				<td>{getData.columns[0].grades[i].user.first_name} {getData.columns[0].grades[i].user.middle_name}</td>
				{getData && getData.columns.map((element, grade_index) => {
				  return <td>{getData.columns[grade_index].grades[i].value}</td>
				})}
			  </tr>
			})}
		  </table>
		</div>

	  </div>
	  </div>
  }
}

