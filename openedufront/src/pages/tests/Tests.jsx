import './tests.css'
import {useEffect, useState} from "react";
import axios from 'axios';
import {useSelector} from "react-redux";
import {useQuery} from 'react-query';

import {useHistory} from "react-router-dom";


export default function Tests() {
  const history = useHistory()
  const lessonId = JSON.parse(localStorage.getItem('test-lesson-id'))

  const {isLoading, error, data} = useQuery('fetchLuke', () =>
	  axios(`http://127.0.0.1:8000/tests/lesson/${lessonId}`, {
		headers: {
		  "Authorization": "JWT " + state.auth.token.access,
		}
	  }))

  const [lessons, setLessons] = useState([])
  const [result, setResult] = useState('')
  const [close, setClose] = useState(true)
  const [modalId, setModalId] = useState(-1)
  const [answers, setAnswers] = useState([])
  const [questions, setlessonsQuestions] = useState([])
  const state = useSelector(state => state)

  useEffect(async () => {
	const lessons = await axios.get(`http://127.0.0.1:8000/tests/lesson/${lessonId}`, {
	  headers: {
		"Authorization": "JWT " + state.auth.token.access,
	  }
	})
	console.log(lessons)
	setLessons(lessons.data)
  }, [])


  const handleFetchingData = async (id) => {

	const lessonsQuestions = await axios.get(`http://127.0.0.1:8000/tests/${id}`, {
	  headers: {
		"Authorization": "JWT " + state.auth.token.access,
	  }
	})
	setlessonsQuestions(lessonsQuestions.data)
  }

  const openModal = (id) => {
	setClose(p => !p)
	setModalId(id)
  }

  const handleSubmit = async () => {
	console.log(answers)
	await axios.post(`http://127.0.0.1:8000/tests/count/${lessonId}`, {"answers": answers.join(' ')}, {
	  headers: {
		"Authorization": "JWT " + state.auth.token.access,
	  }
	},).then((res) => {
	  setResult(res.data.score)
	  setAnswers([])
	})
  }

  if (JSON.parse(localStorage.getItem('test-lesson-id')) === null) history.push('/student/classes')

  return (
	  <div className="tests_wrapper">
		<aside className="aside">
		  {data && data.data.map(el => {
			return <div key={el.id} className={"test"} data-id={el.id} onClick={() => handleFetchingData(el.id)}>
			  <h4>{el.title}</h4>
			  <span>Старт: <i className="">{el.open_since}</i></span>
			  <span>Кінець: <i>{el.open_until}</i></span>
			  <span>Загальний результат: {result}</span>
			</div>
		  })}
		  <button onClick={handleSubmit}>submit</button>
		</aside>
		<main className="tests_main">
		  <div className="tests_container">
			<div className="test_information">
			  <h4>{questions.title}</h4>
			  <div className="date_tests_container">
				<div className="date_information">
				  <span>Старт: <i className="data">{questions.open_since}</i></span>
				  <span>Кінець: <i className="data">{questions.open_until}</i></span>
				</div>
				{/*<div className="class_name">*/}
				{/*  <span>Фізика</span>*/}
				{/*</div>*/}
			  </div>
			</div>

			<div className="tests_tests_container">
			  {/*<div className="tests_tests_container_test">*/}
			  {/*<span>1</span>*/}
			  {/*<span className="correct wrong no-result"></span>*/}
			  {/*<span>B</span>*/}
			  {/*</div>*/}
			  {questions.questions && questions.questions.map((el, i) => {
				return <div key={el.id} className="tests_tests_container_test"
							onClick={() => openModal(i)}>{i + 1}</div>
			  })}
			</div>
		  </div>
		  <div id="myModal" class="modal" style={{'display': `${close ? 'none' : 'block'}`}}>
			<div class="modal-content">

			  <h1>{questions.questions && questions.questions[modalId] && questions.questions[modalId].text}<span
				  onClick={() => openModal()}>X</span></h1>
			  <div>
				<div class="answers_container">
				  {questions.questions && questions.questions[modalId] && questions.questions[modalId].answers.map((el, i) => {
					return <div className="answer" key={i}>
					  <input
						  type="checkbox"
						  name="rGroup"
						  value={el.text}
						  id={el.text}
						  className="check"
						  onChange={(e) => {
							if (e.target.checked) {
							  setAnswers(p => [...p, el.id])
							} else {
							  setAnswers(p => p.pop())
							}
							console.log(answers)
						  }}
					  />
					  <label className="whatever" htmlFor={el.text}><span>{el.text}</span></label>
					</div>
				  })}
				</div>
			  </div>
			</div>
		  </div>
		</main>
	  </div>
  );

}