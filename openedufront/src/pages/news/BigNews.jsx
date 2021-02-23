import {manageBigText, manageTitle} from "../../helpers/manage";

import {useEffect, useRef, useState} from "react";
import {useSelector} from "react-redux";

import BigModal from "../../components/modal/bigModal";
import {url} from '../../helpers/utils'
import axios from "axios";


function BigNews() {
  const modalRef = useRef()

  const news = useSelector((state) => state.news);
  const auth = useSelector((state) => state.auth);

  const [newsById, setNewsById] = useState(null)


  useEffect(async () => {
    try {
	  const response = await axios.get(`${url}/news/${news.data.mainNews.id}`, {
		headers: {
		  "Authorization": "JWT " + auth.token.access,
		}
	  })
	  await setNewsById(response.data)
	} catch(e) {
      console.log(e)
	}
  }, [news.data.mainNews])


  if (!news.loading && newsById !== null) {
	const {creation_date, name, mini_description, id} = news.data.mainNews;
	const {creation_date: creation_date_expand, name: name_expand, description: description_expand} = newsById;

	return (
		<section className="intro">
		  <BigModal ref={modalRef}>
			<span>{creation_date_expand}</span>
			<span>{name_expand}</span>
			<span>{description_expand}</span>
		  </BigModal>

		  <div className="left-text">
			<h4 className="text-date">{creation_date}</h4>
			<h1 className="text-title">{manageTitle(name)}</h1>
			<p className="text-description">{manageBigText(mini_description)}</p>
			<div className="wrapper-buttons">
			  <a className="check-news" onClick={() => {
				modalRef.current.open()
			  }}>більше</a>
			  <p className="every-week">Свіжі новини</p>
			</div>
		  </div>
		  <div className="right-photo"/>
		</section>
	);
  }
else
  {
	return (
		<div className={"big-news-skeleton"}>
		  <div className="news-skew"/>
		</div>
	);
  }
}

export default BigNews;
