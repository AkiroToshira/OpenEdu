import '../classes.css'

function ClassesStudent() {
  return (
	  <div className="main-container">
		<div className="subjet-title"><span>Предмети</span></div>
		<div className="container">
		  {/*{% for lesson in get_profile.student_group.lessons.all %}*/}
		  {/*<a href="lesson/{{ lesson.id }}" className="col">*/}
			{/*<div className="inner-information"><span>{{lesson.name}}</span><span>Teacher</span></div>*/}
		  {/*</a>*/}
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
			{/*<tr>*/}

			{/*  <td>{{x.lesson}}</td>*/}
			{/*  <td>{{x.name}}</td>*/}
			{/*  <td>{{x.deadline_time}}</td>*/}
			{/*  <td>--</td>*/}
			{/*</tr>*/}
			{/*{% endfor %}*/}
			</tbody>
		  </table>
		</div>
	  </div>
  );
}


export default ClassesStudent;