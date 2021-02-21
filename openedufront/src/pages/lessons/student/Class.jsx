import '../class.css'
import {fetchLessonsStudentDetailed} from "../../../actions/lessonsStudentByid";

import {useEffect} from "react";
import {useDispatch, useSelector} from "react-redux";

function ClassStudent() {
  let dispatch = useDispatch()
  let lessonsStudentById = useSelector(state => state.lessonsStudentById)
  let chapters = lessonsStudentById.detailed.chapters
  let moderators = lessonsStudentById.detailed.lesson_moderator

  useEffect(() => {
    const id = JSON.parse(localStorage.getItem('lessonId'))
	dispatch(fetchLessonsStudentDetailed(id))
  }, [])

  if(!lessonsStudentById.loading) {
  return (
	  <div className="container">
		<div className="first-section">

		  {chapters.map((el,i ) => {
		    return <div className="col" key={el.id}>
			  <div className="title">
				<span>{el.name}</span>
			  </div>
			  <div className="description">
				<span>{el.description}</span>
			  </div>
			  <div className="title pdf">
				скачування ще в розробці^^
			  </div>
			</div>
		  })}
		</div>
		<div className="second-section">
		  <div className="col col-teacher-info">
			<div className="teacher-img" style={{margin: '0 auto'}}/>
			<div className="whois">
			  <span>Викладач:</span>
			  {moderators.map(el => {
			    return <span key={el.id}>{el.last_name} {el.first_name.substring(0,1)} {el.middle_name.substring(0,1)}</span>
			  })}
			</div>
		  </div>
		</div>
	  </div>
  );
	} else {
    return <>
		<div>Loading...</div>
	</>
  }
}


export default ClassStudent;
