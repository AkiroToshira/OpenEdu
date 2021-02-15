import '../classes.css'
import {addDeadlines, updateDeadlines} from "../../../actions/deadlines";
import {useDispatch} from "react-redux";


function Editdeadlines() {
  const dispatch = useDispatch()

  const addDeadline = () => {
	let name = prompt('name ')
	let type = prompt('type ')
	let lesson = 9
	let description = prompt('description ')
	let deadline_time = prompt('deadline_time ')
	let id = 9
	dispatch(updateDeadlines(lesson,name, description, deadline_time, type, id))
  }

  return <form encType="multipart/form-data" action="" method="post">
	{/*{% csrf_token %}*/}
	<div className="flex-container">
	  <div className="col1">
		<div className="subject-title">
		  <label for="id_name">Name:</label>
		  <input type="text" name="name" maxlength="20" required id="id_name" value="{{update_deadline.name}}"/>
		</div>
	  </div>
	  <div className="col1">
		<div className="deadline-time">
		  <label for="id_deadline_time">Deadline time:</label>
		  <input type="date" name="deadline_time" required id="id_deadline_time"
				 value="{{update_deadline.deadline_time}}"/>
		</div>
	  </div>
	  <div className="col1">
		<div className="lesson-check">
		  <label for="id_lesson">Lesson:</label>
		  <select name="lesson" required id="id_lesson">
			<option disabled>Виберіть предмет</option>
			{/*{% for lesson in get_lesson %}*/}
			{/*<option value="{{ lesson.id }}">{{ lesson.name }}</option>*/}
			{/*{% endfor %}*/}
		  </select>
		</div>
	  </div>
	  <div className="col1">
		<div className="group-check">
		  <label for="id_group">Group:</label>
		  <select name="group" required id="id_group">
			<option disabled>Виберіть групу</option>
			{/*{% for group in get_group %}*/}
			{/*<option value="{{ group.id }}">{{ group.name }}</option>*/}
			{/*{% endfor %}*/}
		  </select>
		</div>
	  </div>
	  <div className="col1">
		<div className="modal-add">
		  <button type="submit" name="button" onClick={addDeadline}>Add</button>
		</div>
	  </div>
	</div>
  </form>
}

export default Editdeadlines

