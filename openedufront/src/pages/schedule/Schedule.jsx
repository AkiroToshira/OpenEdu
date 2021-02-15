import './schedule.css'

import {useEffect} from 'react'
import {fetchSchedule} from "../../actions/schedule";
import {useDispatch, useSelector} from "react-redux";
import {fetchLessonsStudentDetailed} from "../../actions/lessonsStudentByid";
import lessonsStudentById from "../../reducer/lessonsStudentById";
import axios from "axios";
import {url} from "../../helpers/utils";
import {useState} from "react";

function Schedule() {
  const dispatch = useDispatch()
  const schedule = useSelector(state => state.schedule)


  // if (!schedule.loading) {
  return (<div className="schedual">
		<div className="schedual_title">
		  <div className="schedule_title_block">Розклад</div>
		  <div className="group_info">
			<div className="first group_block select-1">
			  <div className="left-line" style={{'backgroundColor': 'aquamarine'}}/>
			  1 підгрупа
			</div>
			<div className="second group_block select-2">
			  <div className="left-line" style={{'backgroundColor': 'darkmagenta'}}/>
			  2 підгрупа
			</div>
			<div className="both group_block select-3">
			  <div className="left-line" style={{'backgroundColor': 'black'}}/>
			  Обидві
			</div>
		  </div>
		</div>
		<div className="schedual_block_wrapper">
		  {Object.keys(schedule.days).map((el, i) => <ScheduleBlock key={i} schedule={schedule.days} index={i}/>)}

		</div>
	  </div>
  )
  //
  // } else {
  // return <div>Loading...</div>
  // }

}

function ScheduleBlock({schedule, index}) {
  let days = Object.keys(schedule)
  let weekDay = schedule[days[index]]
  return <>
	<div className="schedual_block">
	  <div className="schedual_block_title">
		<div className="schedual_block_title_wrapper">
		  Понеділок
		  <div className="schedual_block_title_undeline">
		  </div>
		</div>

	  </div>

	  <div className="schedual_block_info">
		<div className="schedual_list">
		  {weekDay.map((el, i) => {
			return <CertainDay data={el}/>
		  })}
		</div>
	  </div>

	</div>
  </>
}

function CertainDay({data}) {
  const {time, subgroup, lesson, addinfo} = data
  const dispatch = useDispatch()
  const teacher = useSelector(state => lessonsStudentById)
  const getState = useSelector(state => state)
  const [teachers, setTeachers] = useState([])
  const [close, setClose] = useState(true)


  useEffect(fetchInfo, [])

  async function fetchInfo() {
	if (addinfo !== null) {
	  try {
		const detailed = await axios.get(`${url}/lessons/student/${addinfo.id}`, {
		  headers: {
			"Authorization": "JWT " + getState.auth.token.access,
		  }
		})
		let teachers = await detailed.data.lesson_moderator
		setTeachers(teachers)
		console.log(teachers)
	  } catch (e) {
		console.log(e)
	  }


	}

  }

  const toggleClose = () => {
	setClose(p => !p)
  }

  return <div className="schedual_list_item_block">
	<div className="item_time">{time}</div>
	<div className="schedual_list_items">
	  <div className="schedual_list_item">
		<div className="item_wrapper" onClick={toggleClose}>
		  <div className="item_wrapper_info">
			{subgroup === "First" ? <div class="left-line" style={{'background-color': 'aquamarine'}}></div> : ''}
			{subgroup === "Second" ? <div class="left-line" style={{'background-color': 'darkmagenta'}}></div> : ''}
			{subgroup === "Both" ? <div class="left-line" style={{'background-color': 'black'}}></div> : ''}
			<div class="subject" >{lesson.lesson.name}</div>
		  </div>
		  <div className="additional_info" style={{'display': `${close ? "none" : "block"}`}}>
			<div className="">
			  Викладачі: {teachers.map(el => {
			  return <span key={el.id}>{el.first_name} {el.middle_name} </span>
			})}
			</div>
			<div className="link">Посилання:<a
				href="https://meet.google.com/nbh-gnci-xnm?pli=1&authuser=2">перейти</a>
			</div>
			<div className="">Дод. інформація: {addinfo === null ? "нічого" : addinfo.info}</div>
		  </div>
		</div>
	  </div>
	</div>
  </div>
}

export default Schedule