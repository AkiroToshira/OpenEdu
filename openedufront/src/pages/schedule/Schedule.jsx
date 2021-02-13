import './schedule.css'

import {useEffect} from 'react'
import {fetchSchedule} from "../../actions/schedule";
import {useDispatch, useSelector} from "react-redux";

function Schedule() {
  const dispatch = useDispatch()
  const schedule = useSelector(state => state.schedule)


  useEffect(() => {
	dispatch(fetchSchedule())
  }, [])
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
			{Object.keys(schedule.days).map((_, i) => <ScheduleBlock key={i}/>)}

		  </div>
		</div>
	)
  //
  // } else {
	// return <div>Loading...</div>
  // }

}

function ScheduleBlock({dayName}) {
  return <>
	<div className="schedual_block">
	  <div className="schedual_block_title">
		<div className="schedual_block_title_wrapper">
		  Понеділок
		  <div className="schedual_block_title_undeline">
		  </div>
		</div>
		{/*<div className="schedual_block_info">*/}
		{/*  <div className="schedual_list">*/}
		{/*	/!*{% for x in schedule_monday%}*!/*/}
		{/*	<div className="schedual_list_item_block">*/}
		{/*	  /!*<div class="item_time">{{ x.time }}</div>*!/*/}
		{/*	  <div className="schedual_list_items">*/}
		{/*		<div className="schedual_list_item">*/}
		{/*		  <div className="item_wrapper">*/}
		{/*			<div className="item_wrapper_info">*/}
		{/*			  /!*  {% if x.subgroup == 'First'%}*!/*/}
		{/*			  /!*  <div class="left-line" style='background-color: aquamarine;' data-group=1></div>*!/*/}
		{/*			  /!*{% endif %}*!/*/}
		{/*			  /!*{% if x.subgroup == 'Second'%}*!/*/}
		{/*			  /!*<div class="left-line" style='background-color: darkmagenta;'*!/*/}
		{/*			  /!*	 data-group=2></div>*!/*/}
		{/*			  /!*{% endif %}*!/*/}
		{/*			  /!*{% if x.subgroup == 'Both'%}*!/*/}
		{/*			  /!*<div class="left-line" style='background-color: black;' data-group=3*!/*/}
		{/*			  /!*></div>*!/*/}
		{/*			  /!*{% endif %}*!/*/}
		{/*			  /!*<div class="subject">{{ x.lesson }}</div>*!/*/}
		{/*			</div>*/}
		{/*			<div className="additional_info">*/}
		{/*			  <div className="">*/}
		{/*				/!*Викладачі: {% for i in x.lesson.get_lesson_teachers %}*!/*/}
		{/*				/!*{{ i.get_full_name }}*!/*/}
		{/*				/!*{% endfor %}*!/*/}
		{/*			  </div>*/}
		{/*			  <div className="link">Посилання:<a*/}
		{/*				  href="https://meet.google.com/nbh-gnci-xnm?pli=1&authuser=2">перейти</a>*/}
		{/*			  </div>*/}
		{/*			  <div className="">Дод. інформація: Контрольна робота</div>*/}
		{/*			</div>*/}
		{/*		  </div>*/}
		{/*		</div>*/}
		{/*	  </div>*/}
		{/*	</div>*/}
		{/*	/!*{% endfor %}*!/*/}
		{/*  </div>*/}
		{/*</div>*/}
	  </div>
	</div>
  </>
}

export default Schedule