import '../classes.css'


function Editdeadlines() {
  return <form enctype="multipart/form-data" action="" method="post">
	{/*{% csrf_token %}*/}
	<div class="flex-container">
	  <div class="col1">
		<div class="subject-title">
		  <label for="id_name">Name:</label>
		  <input type="text" name="name" maxlength="20" required id="id_name" value="{{update_deadline.name}}"/>
		</div>
	  </div>
	  <div class="col1">
		<div class="deadline-time">
		  <label for="id_deadline_time">Deadline time:</label>
		  <input type="date" name="deadline_time" required id="id_deadline_time"
				 value="{{update_deadline.deadline_time}}"/>
		</div>
	  </div>
	  <div class="col1">
		<div class="lesson-check">
		  <label for="id_lesson">Lesson:</label>
		  <select name="lesson" required id="id_lesson">
			<option disabled>Виберіть предмет</option>
			{/*{% for lesson in get_lesson %}*/}
			{/*<option value="{{ lesson.id }}">{{ lesson.name }}</option>*/}
			{/*{% endfor %}*/}
		  </select>
		</div>
	  </div>
	  <div class="col1">
		<div class="group-check">
		  <label for="id_group">Group:</label>
		  <select name="group" required id="id_group">
			<option disabled>Виберіть групу</option>
			{/*{% for group in get_group %}*/}
			{/*<option value="{{ group.id }}">{{ group.name }}</option>*/}
			{/*{% endfor %}*/}
		  </select>
		</div>
	  </div>
	  <div class="col1">
		<div class="modal-add">
		  <button type="submit" name="button">Add</button>
		</div>
	  </div>
	</div>
  </form>
}

export default Editdeadlines

