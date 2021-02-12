import {
  FETCH_LESSONS_STUDENT_BY_ID, FETCH_LESSONS_STUDENT_BY_ID_FAIL, FETCH_LESSONS_STUDENT_BY_ID_SUCCESS,
} from "./types";

import axios from "axios";
import {url} from "../helpers/utils";

export const fetchLessonsStudentDetailed = (id) => async (dispatch, getState) => {
  dispatch({
	type: FETCH_LESSONS_STUDENT_BY_ID,
  })
  try {
	const detailed = await axios.get(`${url}/lessons/student/${id}`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_LESSONS_STUDENT_BY_ID_SUCCESS,
	  payload: detailed.data,
	})
  } catch(e) {
	dispatch({
	  type: FETCH_LESSONS_STUDENT_BY_ID_FAIL,
	  error: e,
	})
  }
}