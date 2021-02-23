import axios from "axios";
import {url} from "../helpers/utils";
import {
  FETCH_GRADES_LESSONS,
  FETCH_GRADES_LESSONS_FAIL,
  FETCH_GRADES_LESSONS_SUCCESS,
  FETCH_TEACHER_GRADES, FETCH_TEACHER_GRADES_FAIL, FETCH_TEACHER_GRADES_SUCCESS
} from "./types";

export const fetchGradesLessons = () => async (dispatch, getState) => {
  dispatch({
	type: FETCH_GRADES_LESSONS,
  })
  try {
	const lessons = await axios.get(`${url}/gradebook/gradebooklist/`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_GRADES_LESSONS_SUCCESS,
	  payload: lessons.data,
	})
  } catch (e) {
	dispatch({
	  type: FETCH_GRADES_LESSONS_FAIL,
	  error: e,
	})
  }
}

export const fetchTeacherGradesLessons = (id) => async (dispatch, getState) => {
  dispatch({
	type: FETCH_TEACHER_GRADES,
  })
  try {
	const lessonGrades = await axios.get(`${url}/gradebook/teacher/${id}`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_TEACHER_GRADES_SUCCESS,
	  payload: lessonGrades.data,
	})
  } catch (e) {
	dispatch({
	  type: FETCH_TEACHER_GRADES_FAIL,
	  error: e,
	})
  }
}

export const updateGrade = (id, value, col) => async (dispatch, getState) => {
  try {
    await axios.put(`${url}/gradebook/teacher/grade/`, {
	  id,
	  value
	}, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: "UPDATE_TEACHER_GRADE",
	  payload: {id, value, col},
	})
  } catch (e) {
	dispatch({
	  type: FETCH_TEACHER_GRADES_FAIL,
	  error: e,
	})
  }
}