import {useContext} from "react";
import {Context} from "../../context";
import {manageBigText, manageTitle} from "./manage";
import useFetch from "../../use/useFetch";
import {url} from "../../utils";

function BigNews() {
  // const {news, newsLoading} = useContext(Context)
  // const [news, newsLoading] = useFetch(`${url}/news/`)
  // const [news, newsLoading] = useFetch(`${url}/news/`)
	const creation_date = '', name = '', mini_description = ''

	// const {creation_date, name, mini_description} = news[0]
	return <section className="intro">
	  <div className="left-text">
		<h4 className="text-date">{creation_date}
		</h4>
		<h1 className="text-title">{manageTitle(name)}
		</h1>
		<p className="text-description">{manageBigText(mini_description)}</p>
		<div className="wrapper-buttons">
		  <a className="check-news">більше</a>
		  <p className="every-week">Новини - кожного тижня</p>
		</div>
	  </div>
	  <div className="right-photo"></div>
	</section>
  // } else {
	// return <div className={"big-news-skeleton"}>
	// 	<div className="news-skew"></div>
	// </div>
  // }
}

export default BigNews