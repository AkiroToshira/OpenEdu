import axios from "axios";
import {url} from "../helpers/utils";
import {ADD_DEADLINES, FETCH_DEADLINES, FETCH_DEADLINES_FAIL, FETCH_DEADLINES_SUCCESS} from "./types";

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
  } catch (e) {
	dispatch({
	  type: FETCH_DEADLINES_FAIL,
	  error: e,
	})
  }
}

export const deleteDeadlines = (id) => async (dispatch, getState) => {
  try {
	await axios.delete(`${url}/deadlines/delete`, {
	  data: {"id": id},
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({type: "DELETE_DEADLINES", payload: id})
  } catch (e) {
	dispatch({
	  type: FETCH_DEADLINES_FAIL,
	  error: e,
	})
  }
}

export const addDeadlines = ({lesson, name, description, deadline_time, type}) => async (dispatch, getState) => {
  try {

	const detailed = await axios.post(`${url}/deadlines/create`, {lesson, name, description, deadline_time, type}, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_DEADLINES,
	})
	dispatch({
	  type: ADD_DEADLINES,
	  payload: detailed.data,
	})

  } catch (e) {
	dispatch({
	  type: FETCH_DEADLINES_FAIL,
	  error: e,
	})
  }
}


export const updateDeadlines = ({lesson,name, description, deadline_time, type, id}) => async (dispatch, getState) => {
  try {
	const getLessonId = await axios.get(`${url}/gradebook/gradebooklist/`,  {headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }})
	let lessonId = getLessonId.data.filter(el => el.lesson.id === lesson)[0]

	await axios.put(`${url}/deadlines/update`, {lesson: lessonId.id, name, description, deadline_time, type, id}, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_DEADLINES,
	})
	dispatch({
	  type: "UPDATE_DEADLINES",
	  payload: {lesson: lessonId.id, name, description, deadline_time, type, id},
	})
  } catch (e) {
	dispatch({
	  type: FETCH_DEADLINES_FAIL,
	  error: e,
	})
  }
}