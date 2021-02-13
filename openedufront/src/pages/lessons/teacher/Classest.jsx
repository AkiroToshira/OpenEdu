import '../classes.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from "react";
import {fetchLessonsTeacher} from "../../../actions/lessonsTeacher";
import {fetchDeadlines} from "../../../actions/deadlines";

function Classest() {
  const dispatch = useDispatch()
  const state = useSelector(state => state.lessonsTeacher)
  const deadlines = useSelector(state => state.deadlines)


  useEffect(() => {
	dispatch(fetchLessonsTeacher())
	dispatch(fetchDeadlines())

  }, [])

  return (<>
	<div className="main-container">
	  <div className="subject-title"><span>Предмети</span></div>

	  <div className="inner-container">
		{/*{% for lesson in get_lesson %}*/}
		{state.lessons.map((el) => {
		  return <a href="#" className="col2" key={el.id}>
			<div className="inner-information">
			  <span>{el.name}</span>
			</div>
		  </a>
		})}
		{/*<a href="lesson/{{ lesson.id }}" class="col2">*/}
		{/*    <div class="inner-information"><span>{{ lesson.name }}</span></div>*/}
		{/*</a>*/}
		{/*{% endfor %}*/}
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
				<th colSpan="2" id="myBtn">Додати дедлайн</th>
			  </tr>
			  </thead>
			  <tbody>
			  {deadlines.deadlines.map(el => {
				return (
					<tr key={el.id}>

					  <td>{el.name}</td>
					  <td>{el.type}</td>
					  <td>{el.deadline_time}</td>
					  <td>{el.description}</td>
					  <td/>
					</tr>
				)
			  })}

			  </tbody>
			</table>
		  </div>

		</>
	  }

	<div id="myModal" class="modal">
	  <div class="modal-content">
		<span class="close">&times;</span>

		<div class="modal-body">
		  <form enctype="multipart/form-data" action="" method="post">
			{/*{% csrf_token %}*/}
			<div class="subject-title">
			  <label for="id_name">Name:</label>
			  <input type="text" name="name" maxlength="20" required id="id_name" placeholder="Name"/>
			</div>
			<div class="deadline-time">
			  <label for="id_deadline_time">Deadline time:</label>
			  <input type="date" name="deadline_time" required id="id_deadline_time"/>
			</div>
			<div class="lesson-check">
			  <label for="id_lesson">Lesson:</label>
			  <select name="lesson" required id="id_lesson">
				<option disabled>Виберіть предмет</option>
				{/*{% for lesson in get_lesson %}*/}
				{/*<option value="{{ lesson.id }}">{{ lesson.name }}</option>*/}
				{/*{% endfor %}*/}
			  </select>
			</div>
			<div class="group-check">
			  <label for="id_group">Group:</label>
			  <select name="group" required id="id_group">
				<option disabled>Виберіть групу</option>
				{/*{% for group in get_group %}*/}
				{/*<option value="{{ group.id }}">{{group.name}}</option>*/}
				{/*{% endfor %}*/}
			  </select>
			</div>
			<div class="modal-add">
			  <button type="submit" name="button">Add</button>
			</div>
		  </form>
		</div>
	  </div>
	</div>
	</div>
  </>)
}

export default Classest



