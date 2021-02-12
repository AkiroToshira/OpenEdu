import axios from 'axios';

import {url} from '../helpers/utils'
import {FETCH_LESSONS_STUDENT, FETCH_LESSONS_STUDENT_FAIL, FETCH_LESSONS_STUDENT_SUCCESS} from "./types";

export const fetchLessonsStudent = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_LESSONS_STUDENT,
  })
	try {
	  const lesson = await axios.get(`${url}/lessons/student`, {
		headers: {
		  "Authorization": "JWT " + getState().auth.token.access,
		}
	  })

	  dispatch({
		type: FETCH_LESSONS_STUDENT_SUCCESS,
		payload: lesson.data,
	  })
	} catch(e) {
    	dispatch({
		  type: FETCH_LESSONS_STUDENT_FAIL,
		  error: e,
		})
	}
}