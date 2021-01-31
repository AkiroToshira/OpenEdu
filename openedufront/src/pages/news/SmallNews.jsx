import {Context} from '../../context'
import {useContext} from "react";
import {manageDate, manageText, manageTitle} from "./manage";
import useFetch from "../../use/useFetch";
import {url} from "../../utils";


function SmallNews() {

  // const {news, newsLoading} = useContext(Context)
  const creation_date = '', name = '', mini_description = ''

  return <section className="small-news">
	  <h1 className="upcoming-news">Найновіші новини</h1>
	  <div className="small-news-list">
		{/*{news.map((el, i) => <OneNews data={el} key={i}/>)}*/}
	  </div>
	</section>
  // } else {
	// return <section className="small-news">
	//   <h1 className="upcoming-news">Найновіші новини</h1>
	//   <div className="small-news-list">
	// 	{[1, 2, 3, 4, 5].map(el => {
	// 	  return (
	// 		  <div className={"small-news-skeleton one-news"} key={el}>
	// 			<div className="news-skew"></div>
	// 		  </div>
	// 	  )
	// 	})}
	//   </div>
	// </section>
  // }

}

function OneNews(el) {
  const {creation_date, name, mini_description} = el.data


  return <div className="one-news">
	<div className="wrapper-img-date">
	  <div className="small-news-date">
		<span className="date">{manageDate(creation_date)[0]}</span>
		<span className="month">{manageDate(creation_date)[1]}</span>
	  </div>
	  <div className="small-news-photo"></div>
	</div>
	<div className="small-news-text">
	  <div className="small-news-title">{manageTitle(name)}</div>
	  <div
		  className="small-news-description">{manageText(mini_description)}
	  </div>
	  <div className="small-news-check-detailed">Більше про новину</div>
	</div>
  </div>
}

export default SmallNews