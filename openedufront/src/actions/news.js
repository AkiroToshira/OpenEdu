import axios from 'axios';

import {url} from '../helpers/utils'
import {FETCH_NEWS, FETCH_NEWS_FAIL, FETCH_NEWS_SUCCESS} from "./types";

export const newsLogout = () => ({
  type: "LOGOUT",
})

export const fetchNews = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_NEWS,
  })
	try {
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
	} catch(e) {
    dispatch({
	  type: FETCH_NEWS_FAIL,
	  error: e,
	})
	}
}