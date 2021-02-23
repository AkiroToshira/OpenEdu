import '../class.css'
import {useDispatch, useSelector} from "react-redux";
import {useEffect, useRef, useState} from "react";
import {
  addChapter,
  deleteChapter,
  fetchLessonsTeacherDetailed,
  updateChapter
} from "../../../actions/lessonsTeacherByid";
import SmallModal from "../../../components/modal/smallModal";


function Lessont() {
  const dispatch = useDispatch()
  let lessonsTeacherById = useSelector(state => state.lessonsTeacherById)
  let chapters = lessonsTeacherById.detailed.chapters
  const smallRef = useRef()

  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [upd, setUpd] = useState(false)


  useEffect(() => {
	const id = JSON.parse(localStorage.getItem('lessonId'))
	dispatch(fetchLessonsTeacherDetailed(id))
  }, [])

  const handleAddChapter = (e) => {
	e.preventDefault()
	let lesson = JSON.parse(localStorage.getItem('lessonId'))
	dispatch(addChapter(name, description, lesson))
	smallRef.current.end()
  }

  const handleDeleteChapter = (id) => {
	dispatch(deleteChapter(id))
  }

  const handleUpdateChapter = (e) => {
	e.preventDefault()
	let lesson = JSON.parse(localStorage.getItem('lessonId'))
	let id = JSON.parse(localStorage.getItem('reg-id'))
	dispatch(updateChapter(lesson, name, description, id))
	smallRef.current.end()
	setUpd(false)


  }

  if (!lessonsTeacherById.loading) {
	return <>
	  <SmallModal ref={smallRef}>
		<input type={"name"} placeholder={"name"} onChange={(e) => setName(e.target.value)}/>
		<input type={"description"} placeholder={"name"} onChange={(e) => setDescription(e.target.value)}/>
		{!upd && <input type={"submit"} value={"Додавання"} onClick={(e) => handleAddChapter(e)}/>}
		{upd && <input type={"submit"} value={"редагувати"} onClick={(e) => handleUpdateChapter(e)}/>}
	  </SmallModal>
	  <div className="container">
		<div className="first-section">

		  {/*{% for i in get_chapter %}*/}
		  {chapters.map(el => {
			return <div className="col" key={el.id}>
			  <div className="title">
				<span>{el.name}</span>
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
				<a onClick={() => {
				  setUpd(true)
				  localStorage.setItem('reg-id', JSON.stringify(el.id))
				  smallRef.current.add()
				}}>
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
        </span>
			  <hr/>
			  <span className="subject_description">
				{lessonsTeacherById.detailed.description}
			  </span>
			</div>
			{/*<div className="teacher-info"><p>{{get_lesson.description}}</p></div>*/}
			<div className="whois">
			  {/*<span>Групи:</span>*/}
			  {/*{% for i in get_group %}*/}
			  {/*<span>{{i}}</span>*/}
			  {/*{% endfor %}*/}
			</div>
		  </div>
		  <div className="col col-teacher-info add-new-chapter">
			<span className="collapsible" onClick={(e) => {
			  smallRef.current.add()
			}}>Додати</span>
			<div className="content">
			  <form encType="multipart/form-data" action="" method="post">

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
