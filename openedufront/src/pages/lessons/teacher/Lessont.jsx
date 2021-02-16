import '../class.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from "react";
import {fetchLessonsTeacher} from "../../../actions/lessonsTeacher";
import {fetchLessonsStudentDetailed} from "../../../actions/lessonsStudentByid";
import {
  addChapter,
  deleteChapter,
  fetchLessonsTeacherDetailed,
  updateChapter
} from "../../../actions/lessonsTeacherByid";


function Lessont() {
  const dispatch = useDispatch()
  let lessonsTeacherById = useSelector(state => state.lessonsTeacherById)
  let chapters = lessonsTeacherById.detailed.chapters


  useEffect(() => {
	const id = JSON.parse(localStorage.getItem('lessonId'))
	dispatch(fetchLessonsTeacherDetailed(id))
  }, [])

  const handleAddChapter = () => {
	let lesson = JSON.parse(localStorage.getItem('lessonId'))
	let name = prompt("name ")
	let description = prompt("description ")
	dispatch(addChapter(name, description, lesson))
  }

  const handleDeleteChapter = (id) => {
	dispatch(deleteChapter(id))
  }

  const handleUpdateChapter = (id) => {
	let lesson = JSON.parse(localStorage.getItem('lessonId'))
	let name = prompt("name ")
	let description = prompt("description ")
    dispatch(updateChapter(lesson,name, description, id))
  }

  if (!lessonsTeacherById.loading) {
	return <>

	  <div className="container">
		<div className="first-section">

		  {/*{% for i in get_chapter %}*/}
		  {chapters.map(el => {
			return <div className="col">
			  <div className="title">
				<span>{el.name} {el.id}</span>
			  </div>
			  <div className="description">
				<span>{el.description}</span>
			  </div>
			  <div className="title pdf">
				{/*<a href="{{ i.document.url }}" download>{{i.document.name}}</a>*/}
				{/*<img src="../../media/page/pdf.svg" alt="" className="user-png">*/}
			  </div>
			  <div className="redaction">
				<a onClick={() => handleDeleteChapter(el.id)}>Видалити</a>
				<a onClick={() => handleUpdateChapter(el.id)}>
				  <span>Редактувати</span>
				</a>
			  </div>
			</div>
		  })}

		</div>
		<div className="second-section">

		  <div className="col col-teacher-info">
			<div className="title">
			  <span>
				{lessonsTeacherById.detailed.name}
				<hr/>
				{lessonsTeacherById.detailed.description}
			  </span>
			</div>
			{/*<div className="teacher-info"><p>{{get_lesson.description}}</p></div>*/}
			<div className="whois">
			  <span>Групи:</span>
			  {/*{% for i in get_group %}*/}
			  {/*<span>{{i}}</span>*/}
			  {/*{% endfor %}*/}
			</div>
		  </div>
		  <div className="col col-teacher-info add-new-chapter">
			<span className="collapsible" onClick={(e) => handleAddChapter(e)}>Додати</span>
			<div className="content">
			  <form encType="multipart/form-data" action="" method="post">
				{/*{% csrf_token %}*/}
				{/*{{form.as_p}}*/}
				<div className="modal-footer">
				  <button type="submit" name="button">Add</button>
				</div>
			  </form>
			</div>
		  </div>

		</div>

	  </div>
	</>
  } else {
  }
  return (
	  <div>Loading...</div>
  )
}

export default Lessont

