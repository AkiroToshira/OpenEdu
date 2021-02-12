import axios from "axios";
import {url} from "../helpers/utils";
import {FETCH_DEADLINES, FETCH_DEADLINES_FAIL, FETCH_DEADLINES_SUCCESS} from "./types";

export const fetchDeadlines = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_DEADLINES,
  })
  try {
	const detailed = await axios.get(`${url}/deadlines/`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_DEADLINES_SUCCESS,
	  payload: detailed.data,
	})
  } catch(e) {
	dispatch({
	  type: FETCH_DEADLINES_FAIL,
	  error: e,
	})
  }
}