import {manageBigText, manageTitle} from "../../helpers/manage";

import {useEffect, useContext, useState} from "react";
import {fetchNews} from "../../actions/news";
import {useDispatch, useSelector} from "react-redux";

function BigNews() {
  const dispatch = useDispatch()
  const news = useSelector(state => state.news)

  useEffect(() => {
	dispatch(fetchNews())
  }, [])

  if (!news.loading) {
	const {creation_date, name, mini_description} = news.data.mainNews

	return <section className="intro">
	  <div className="left-text">
		<h4 className="text-date">{creation_date}
		</h4>
		<h1 className="text-title">{manageTitle(name)}
		</h1>
		<p className="text-description">{manageBigText(mini_description)}</p>
		<div className="wrapper-buttons">
		  <a className="check-news">більше</a>
		  <p className="every-week">Свіжі новини</p>
		</div>
	  </div>
	  <div className="right-photo"/>
	</section>
  } else {
	return <div className={"big-news-skeleton"}>
	  <div className="news-skew"/>
	</div>
  }
}

export default BigNews