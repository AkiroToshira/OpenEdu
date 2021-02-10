import axios from 'axios';

import {url} from '../helpers/utils'
import {FETCH_NEWS, FETCH_NEWS_SUCCESS} from "./types";

export const fetchNews = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_NEWS,
  })
  const response = await axios.get(`${url}/news/`, {
	headers: {
	  "Authorization": 'JWT ' + getState().auth.token.access,
	}
  });
  dispatch({
	type: FETCH_NEWS_SUCCESS,
	payload: {
	  mainNews: response.data[0],
	  smallNews: response.data.filter((_, i) => i !== 0),
	}
  })
}