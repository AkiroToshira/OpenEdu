import axios from 'axios'
import {FETCH_LESSONS_TEACHER, FETCH_LESSONS_TEACHER_FAIL, FETCH_LESSONS_TEACHER_SUCCESS} from "./types";
import {url} from "../helpers/utils";

export const fetchLessonsTeacher = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_LESSONS_TEACHER
  })
  try {

	const response = await axios.get(`http://127.0.0.1:8000/lessons/teacher`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_LESSONS_TEACHER_SUCCESS,
	  payload: response.data,
	})
  } catch (e) {
    console.log(e)
	dispatch({
	  type: FETCH_LESSONS_TEACHER_FAIL,
	  error: e,
	})
  }
}