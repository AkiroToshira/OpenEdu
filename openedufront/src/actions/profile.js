import axios from "axios";

import {url} from '../helpers/utils'
import {FETCH_PROFILE, FETCH_PROFILE_FAIL, FETCH_PROFILE_ID_AND_STATUS, FETCH_PROFILE_SUCCESS} from "./types";

export const profileLogout = () => ({
  type: "LOGOUT",
})

export const fetchProfile = () => async (dispatch, getState) => {

  dispatch({
	type: FETCH_PROFILE,
  })
  try {
	const user = await axios.get(`${url}/user/react-info/`, {
	  headers: {
		"Authorization": 'JWT ' + getState().auth.token.access,
	  }
	})

	const response = await axios.get(`${url}/user/${user.data.id}`, {
	  headers: {
		"Authorization": 'JWT ' + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_PROFILE_SUCCESS,
	  payload: {...response.data, ...user.data}
	})
  } catch (e) {
	dispatch({
	  type: FETCH_PROFILE_FAIL,
	  error: e,
	})
  }
}