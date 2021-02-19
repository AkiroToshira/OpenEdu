import {useQuery} from "react-query";
import axios from "axios";
import {useSelector} from "react-redux";
import {useEffect, useState} from "react";

import './grade.css'

function Grades() {
  const state = useSelector(state => state)

  const {isLoading, error, data} = useQuery('fetchGradesStudent', () =>
	  axios(`http://127.0.0.1:8000/gradebook/student`, {
		headers: {
		  "Authorization": "JWT " + state.auth.token.access,
		}
	  }))


  const handleExpandClick = (e) => {
	let display = e.target.nextSibling.style.display;
	e.target.nextSibling.style.display = display === 'block' ? 'none' : 'block'
  }

  if (isLoading) {
	return <div>Loading...</div>
  }


  if (!isLoading) {
    console.log(data)
	return (
		<div className="grades_wrapper">
		  <div className="grades_list">
			{data.data.map((el, i) => {
			  return <div className="grade_element" key={el.id}>
				<div className="grade_title" onClick={(e) => handleExpandClick(e)}>{el.lesson.name}</div>
				<div className="expand_details">
				  <table>
					<tr>
					  {el.gradebook ? <th>Студенти</th> : <th>Пусто</th>}
					  {el.gradebook && el.gradebook.columns.map((el, i) => {
						return <th>{el.date}</th>
					  })}
					  {/*<th>Company</th>*/}
					  {/*<th>Contact</th>*/}
					  {/*<th>Country</th>*/}
					</tr>
					  {el.gradebook && [...new Array(el.gradebook.columns[0].grades.length)].map((item, i) => {
						return 	<tr>
						  <td>{el.gradebook.columns[0].grades[i].user.first_name} {el.gradebook.columns[0].grades[i].user.middle_name}</td>
						  {el.gradebook && el.gradebook.columns.map((element, grade_index) => {
							// {console.log(el.gradebook)}
						  return <td>{el.gradebook.columns[grade_index].grades[i].value}</td>
						  })}
						</tr>
					  })}
				  </table>


				</div>
			  </div>
			})}
		  </div>
		</div>
	)
  }
}

export default Grades;