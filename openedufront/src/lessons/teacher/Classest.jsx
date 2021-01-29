import '../classes.css'

function Classest() {
  return (<>
	<div class="main-container">
	  <div class="subjet-title"><span>Предмети</span></div>

	  <div class="container">
		{/*{% for lesson in get_lesson %}*/}
		{/*<a href="lesson/{{ lesson.id }}" class="col">*/}
		{/*    <div class="inner-information"><span>{{ lesson.name }}</span></div>*/}
		{/*</a>*/}
		{/*{% endfor %}*/}
	  </div>

	  <div class="subjet-title">
		<div>
		  <span>Дедлайни</span>
		</div>
	  </div>
	  <div class="deadline-container">
		<table class="content-table">
		  <thead>
		  <tr>
			<th>Назва предмата</th>
			<th>Назва задачі</th>
			<th>Дедлайн</th>
			<th>Група</th>
			<th colspan="2" id="myBtn">Додати дедлайн</th>
		  </tr>
		  </thead>
		</table>
	  </div>
	</div>
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
  </>)
}

export default Classest



