import './schedule.css'

function Schedule() {
  return (<div className="schedule">
	<h1 className="schedule-title">Розклад</h1>
	<div className="schedule-block-wrapper">
	  {["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"].map((el, i) => <ScheduleBlock key={i} dayName={el}/>)}

	</div>
  </div>)
}

function ScheduleBlock({dayName}) {
  return <div className="schedule-block">
	<div className="schedule-head">
	  <div>{dayName}</div>
	</div>
	<div className="schedule-body"></div>
  </div>
}

export default Schedule