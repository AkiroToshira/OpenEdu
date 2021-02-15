import '../classes.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from "react";
import {useHistory} from "react-router-dom";
import {addDeadlines, deleteDeadlines, fetchDeadlines, updateDeadlines} from "../../../actions/deadlines";
import {fetchLessonsTeacherDetailed} from "../../../actions/lessonsTeacherByid";
import {AiOutlineDelete, AiOutlineEdit} from "react-icons/all";
import {url} from "../../../helpers/utils";

function Classest() {
  const history = useHistory()
  const dispatch = useDispatch()
  const state = useSelector(state => state.lessonsTeacher)
  const deadlines = useSelector(state => state.deadlines)


  useEffect(() => {
	dispatch(fetchDeadlines())

  }, [])

  const handleLessonClick = (id) => {
	dispatch(fetchLessonsTeacherDetailed(id))
	localStorage.setItem("lessonId", JSON.stringify(id))
	history.push("/teacher/lessont");
  }

  const addDeadline = () => {
	let name = prompt('name ')
	let type = prompt('type ')
	let lesson = 9
	let description = prompt('description ')
	let deadline_time = prompt('deadline_time ')
	dispatch(addDeadlines(lesson, name, description, deadline_time, type))
  }

  const deleteDeadline = (id) => {
	dispatch(deleteDeadlines(id))
  }

  const updateDeadline = async (id, lesson) => {
	let name = prompt('name ')
	let type = prompt('type ')
	let description = prompt('description ')
	let deadline_time = prompt('deadline_time ')
	dispatch(updateDeadlines(lesson, name, description, deadline_time, type, id))
  }

  return (<>
	<div className="main-container">
	  <div className="subject-title"><span>Предмети</span></div>

	  <div className="inner-container">
		{state.lessons.map((el) => {
		  return <a href="#" className="col2" key={el.id} onClick={() => handleLessonClick(el.id)}>
			<div className="inner-information">
			  <span>{el.name}</span>
			</div>
		  </a>
		})}
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
				<th colSpan="2" id="myBtn" onClick={addDeadline}>Додати дедлайн</th>
			  </tr>
			  </thead>
			  <tbody>
			  {deadlines.deadlines.map(el => {
				return (
					<tr key={el.id} className={'tr-info'}>

					  <td>{el.name}</td>
					  <td>{el.type}</td>
					  <td>{el.deadline_time}</td>
					  <td>{el.description}</td>
					  <td className="delete" onClick={() => deleteDeadline(el.id)}><AiOutlineDelete/></td>
					  <td className="edit" onClick={() => updateDeadline(el.id, el.lesson.lesson.id)}><AiOutlineEdit/>
					  </td>
					</tr>
				)
			  })}

			  </tbody>
			</table>
		  </div>

		</>
	  }

	  {/*<div id="myModal" class="modal">*/}
	  {/*  <div class="modal-content">*/}
	  {/*	<span class="close">&times;</span>*/}

	  {/*	<div class="modal-body">*/}
	  {/*	  <form enctype="multipart/form-data" action="" method="post">*/}
	  {/*		/!*{% csrf_token %}*!/*/}
	  {/*		<div class="subject-title">*/}
	  {/*		  <label for="id_name">Name:</label>*/}
	  {/*		  <input type="text" name="name" maxlength="20" required id="id_name" placeholder="Name"/>*/}
	  {/*		</div>*/}
	  {/*		<div class="deadline-time">*/}
	  {/*		  <label for="id_deadline_time">Deadline time:</label>*/}
	  {/*		  <input type="date" name="deadline_time" required id="id_deadline_time"/>*/}
	  {/*		</div>*/}
	  {/*		<div class="lesson-check">*/}
	  {/*		  <label for="id_lesson">Lesson:</label>*/}
	  {/*		  <select name="lesson" required id="id_lesson">*/}
	  {/*			<option disabled>Виберіть предмет</option>*/}
	  {/*			/!*{% for lesson in get_lesson %}*!/*/}
	  {/*			/!*<option value="{{ lesson.id }}">{{ lesson.name }}</option>*!/*/}
	  {/*			/!*{% endfor %}*!/*/}
	  {/*		  </select>*/}
	  {/*		</div>*/}
	  {/*		<div class="group-check">*/}
	  {/*		  <label for="id_group">Group:</label>*/}
	  {/*		  <select name="group" required id="id_group">*/}
	  {/*			<option disabled>Виберіть групу</option>*/}
	  {/*			/!*{% for group in get_group %}*!/*/}
	  {/*			/!*<option value="{{ group.id }}">{{group.name}}</option>*!/*/}
	  {/*			/!*{% endfor %}*!/*/}
	  {/*		  </select>*/}
	  {/*		</div>*/}
	  {/*		<div class="modal-add">*/}
	  {/*		  <button type="submit" name="button">Add</button>*/}
	  {/*		</div>*/}
	  {/*	  </form>*/}
	  {/*	</div>*/}
	  {/*  </div>*/}
	  {/*</div>*/}
	</div>
  </>)
}

export default Classest



