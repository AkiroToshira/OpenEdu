import {manageDate, manageText, manageTitle} from "../../helpers/manage";
import {useDispatch, useSelector} from "react-redux";
import {useEffect, useState} from "react";


function SmallNews() {
  const dispatch = useDispatch()
  const smallNews = useSelector(state => state.news)


  if (!smallNews.loading) {
	return <section className="small-news">
	  <h1 className="upcoming-news">Найсвіжіні Новини</h1>
	  <div className="small-news-list">
		{smallNews.data.smallNews.map((el, i) => <OneNews data={smallNews.data.smallNews[i]} key={i}/>)}
	  </div>
	</section>
  } else {
	return <section className="small-news">
	  <div className="small-news-list">
		{[1, 2, 3, 4, 5].map(el => {
		  return (
			  <div className={"small-news-skeleton one-news"} key={el}>
				<div className="news-skew"/>
			  </div>
		  )
		})}
	  </div>
	</section>
  }

}

function OneNews(el) {
  const {creation_date, name, mini_description} = el.data
  const [showPopup, setShowPopup] = useState(false);


  const openSmallNews = () => {
	setShowPopup(true);
  }
  return <div className="one-news">
	<div className="wrapper-img-date">
	  <div className="small-news-date">
		<span className="date">{manageDate(creation_date)[0]}</span>
		<span className="month">{manageDate(creation_date)[1]}</span>
	  </div>
	  <div className="small-news-photo"/>
	</div>
	<div className="small-news-text">
	  <div className="small-news-title">{manageTitle(name)}</div>
	  <div
		  className="small-news-description">{manageText(mini_description)}
	  </div>
	  <div className="small-news-check-detailed" onClick={openSmallNews}>Більше про новину</div>
	</div>
  </div>
}

export default SmallNews