import './tests.css'
import {useEffect, useState} from "react";
import axios from 'axios';
import {useDispatch, useSelector} from "react-redux";
import {useQuery} from 'react-query';

import {useHistory} from "react-router-dom";
import {fetchTests, fetchTestsQuestions} from "../../actions/tests";
import {AiFillCloseCircle} from "react-icons/all";


export default function Tests() {
  const history = useHistory()
  const dispatch = useDispatch()
  const auth = useSelector(state => state.auth)
  const tests = useSelector(state => state.tests)
  const [result, setResult] = useState(JSON.parse(localStorage.getItem('my-grade')) ?? 0)
  const [selectId, setSelectId] = useState(-1)

  const lessonId = JSON.parse(localStorage.getItem('test-lesson-id'))
  if (lessonId === null) history.push('/student/classes')

  useEffect(() => {
	dispatch(fetchTests(lessonId))
  }, [])


  const [close, setClose] = useState(true)
  const [modalId, setModalId] = useState(-1)
  const [answers, setAnswers] = useState([])


  const openModal = (id) => {
	setClose(p => !p)
	setModalId(id)
  }


  const handleQuestions = (id, i) => {
	dispatch(fetchTestsQuestions(id))
	setSelectId(i)
  }


  const handleSubmit = async () => {
	let count = await axios.post(`http://127.0.0.1:8000/tests/count/${lessonId}`, {"answers": answers.join(' ')}, {
	  headers: {
		"Authorization": "JWT " + auth.token.access,
	  }
	},).then((res) => {
	  setResult(res.data.score)
	  setAnswers([])
	  localStorage.setItem('my-grade', JSON.stringify(res.data.score))
	})
  }

  if (!tests.loading) {
	let questions = tests.tests
	return (
		<div className="tests_wrapper">
		  <aside className="tests_aside">
			{questions && questions.map((el, i) => {
			  return <div key={el.id} className={"test"} data-id={el.id} onClick={() => handleQuestions(el.id, i)}>
				<h4>{el.title}</h4>
				<span><i className="">{el.open_since}</i></span>
				<span><i>{el.open_until}</i></span>
				<div className="test_result"><span>{result}</span></div>
			  </div>
			})}
		  </aside>
		  <main className="tests_main">
			{selectId !== -1 && <div className="tests_main_container">
			  <div className="test_information">
				<h4>{tests.tests[selectId].title}</h4>
				<div className="date_tests_container">
				  <div className="date_information">
					<span>Старт: <i className="data">{tests.tests[selectId].open_since}</i></span>
					<span>Кінець: <i className="data">{tests.tests[selectId].open_until}</i></span>
				  </div>
				  <div className="submit_button">
					<button onClick={handleSubmit}>Submit</button>
				  </div>
				</div>

			  </div>

			  <div className="tests_container">
				{tests.questions.questions && tests.questions.questions.map((el, i) => {
				  return <div key={el.id} className="tests_container_test"
							  onClick={() => openModal(i)}>{i + 1}</div>
				})}
			  </div>
			</div>}


			<div id="myModal" class="modal" style={{'display': `${close ? 'none' : 'block'}`}}>
			  <div class="modal-content">

				<h1>{tests.questions.questions && tests.questions.questions[modalId] && tests.questions.questions[modalId].text}<span
					onClick={() => openModal()}><AiFillCloseCircle/></span></h1>
				<div>
				  <div class="answers_container">
					{tests.questions.questions && tests.questions.questions[modalId] && tests.questions.questions[modalId].answers.map((el, i) => {
					  return <div className="answer" key={i}>
						<input
							type="checkbox"
							name="rGroup"
							value={el.text}
							id={el.text}
							className="check"
							onChange={(e) => {
							  if (e.target.checked) {
								  setAnswers([...answers, el.id])
							  } else {
								setAnswers(lastItems=>lastItems.filter((item, i) => item !== el.id))
							  }
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
  } else {
	return <div>Loading...</div>
  }

}
