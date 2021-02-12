import axios from 'axios'
import {FETCH_LESSONS_TEACHER, FETCH_LESSONS_TEACHER_FAIL, FETCH_LESSONS_TEACHER_SUCCESS} from "./types";
import {url} from "../helpers/utils";

export const fetchLessonsTeacher = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_LESSONS_TEACHER
  })
  try {
	const response = await axios.get(`${url}/lessons/teacher`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	console.log(response)
	dispatch({
	  type: FETCH_LESSONS_TEACHER_SUCCESS,
	  payload: response.data,
	})
  } catch (e) {
	dispatch({
	  type: FETCH_LESSONS_TEACHER_FAIL,
	  error: e,
	})
  }
}