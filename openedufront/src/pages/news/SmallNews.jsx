function SmallNews() {
  const data = {
	text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. A amet commodi culpa numquam perspiciatis porro repudiandae, saepe suscipit ullam. Aliquam at dolor, fuga id iste iure labore reprehenderit ut vitae."
  }
  return <section className="small-news">
	<h1 className="upcoming-news">Найновіші новини</h1>
	<div className="small-news-list">
	  {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].map(n => <OneNews text={data} key={n}/>)}

	</div>
  </section>
}

function OneNews({text}) {
  const manageText = ({text}) => {
	if (text.length > 160) {
	  text = text.substring(0, 150)
	}
	return text + '...';
  }

  const manageDate = (date) => date.substring(0,3)

  return <div className="one-news">
	<div className="wrapper-img-date">
	  <div className="small-news-date">
		<span className="date">23</span>
		<span className="month">{manageDate("Грудень")}</span>
	  </div>
	  <div className="small-news-photo"></div>
	</div>
	<div className="small-news-text">
	  <div className="small-news-title">Сьогодні відбулася зустріч випускників</div>
	  <div
		  className="small-news-description">{manageText(text)}
	  </div>
	  <div className="small-news-check-detailed">Більше про новину</div>
	</div>
  </div>
}

export default SmallNews