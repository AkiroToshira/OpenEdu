import './news.css'

import BigNews from "./BigNews";
import SmallNews from "./SmallNews";
import useFetch from "../../use/useFetch";
import {useEffect} from "react";

function NewsPage() {

  return <main>
	<BigNews/>
	<SmallNews/>
  </main>
}

export default NewsPage