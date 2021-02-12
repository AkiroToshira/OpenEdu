import '../classes.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from 'react'
import {fetchLessonsStudent} from "../../../actions/lessonsStudent";

function ClassesStudent() {
  const dispatch = useDispatch();
  const state = useSelector(state => state.lessonsStudent)

  useEffect(() => {
	dispatch(fetchLessonsStudent())
  }, [])

  return (
	  <div className="main-container">
		<div className="subjet-title"><span>Предмети</span></div>
		<div className="inner-container">
		  {/*{% for lesson in get_profile.student_group.lessons.all %}*/}
		  <a href="#" className="col2">
			<div className="inner-information"><span>dkkdk</span><span>Teacher</span></div>
		  </a>
		  <a href="#" className="col2">
			<div className="inner-information"><span>dkkdk</span><span>Teacher</span></div>
		  </a>
		  <a href="#" className="col2">
			<div className="inner-information"><span>dkkdk</span><span>Teacher</span></div>
		  </a>
		  {/*{% endfor %}*/}
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
}


export default ClassesStudent;