import axios from 'axios'

import {url} from '../helpers/utils'
import {FETCH_SCHEDULE, FETCH_SCHEDULE_SUCCESS} from "./types";

export const fetchSchedule = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_SCHEDULE
  })

  const response = await axios.get(`${url}/schedule/`, {
	headers: {
	  "Authorization": "JWT " + getState().auth.token.access
	}
  })

  dispatch({
	type: FETCH_SCHEDULE_SUCCESS,
	payload: response.data
  })
}