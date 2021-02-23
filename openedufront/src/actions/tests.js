import {
  FETCH_LESSONS_STUDENT_BY_ID,
  FETCH_LESSONS_STUDENT_BY_ID_FAIL,
  FETCH_LESSONS_STUDENT_BY_ID_SUCCESS,
  FETCH_TESTS, FETCH_TESTS_FAIL,
  FETCH_TESTS_SUCCESS,
} from "./types";

import axios from "axios";
import {url} from "../helpers/utils";

export const fetchTests = (id) => async (dispatch, getState) => {
  dispatch({
	type: FETCH_TESTS,
  })
  try {
	const tests = await axios.get(`${url}/tests/lesson/${id}`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	console.log(tests.data)
	dispatch({
	  type: FETCH_TESTS_SUCCESS,
	  payload: tests.data,
	})
  } catch(e) {
	dispatch({
	  type: FETCH_TESTS_FAIL,
	  error: e,
	})
  }
}


export const fetchTestsQuestions = (id) => async (dispatch, getState) => {

  try {
	const questions = await axios.get(`${url}/tests/${id}`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	console.log(questions)
	dispatch({
	  type: "FETCH_TESTS_QUESTIONS",
	  payload:  questions.data,
	})
  } catch(e) {
	dispatch({
	  type: FETCH_TESTS_FAIL,
	  error: e,
	})
  }
}