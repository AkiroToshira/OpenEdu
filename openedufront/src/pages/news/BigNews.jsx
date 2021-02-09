import {manageBigText, manageTitle} from "./manage";
import axios from "axios";
import {url} from "../../helpers/utils";
import {useEffect, useContext, useState} from "react";

function BigNews() {

  // useEffect(() => {
	// axios.get(`${url}/news/`, {
	//   headers: {
	// 	Authorization: 'JWT ' + state.access,
	// 	'Content-Type': 'application/json'
	//   }
	// }).then(res => {
	// 	  console.log(res)
	//   setData(res.data)
	//   	setLoaded(true)
	// 	}
	// )
  // }, [])


  if (false) {
	// const {creation_date, name, mini_description} = data[0]
	//
	// return <section className="intro">
	//   <div className="left-text">
	// 	<h4 className="text-date">{creation_date}
	// 	</h4>
	// 	<h1 className="text-title">{manageTitle(name)}
	// 	</h1>
	// 	<p className="text-description">{manageBigText(mini_description)}</p>
	// 	<div className="wrapper-buttons">
	// 	  <a className="check-news">більше</a>
	// 	  <p className="every-week">Свіжі новини</p>
	// 	</div>
	//   </div>
	//   <div className="right-photo"></div>
	// </section>
  } else {
  return <div className={"big-news-skeleton"}>
  	<div className="news-skew"></div>
  </div>
  }
}

export default BigNews