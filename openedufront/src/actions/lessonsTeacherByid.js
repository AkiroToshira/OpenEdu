import {
  FETCH_DEADLINES_FAIL,
  FETCH_LESSONS_TEACHER_BY_ID,
  FETCH_LESSONS_TEACHER_BY_ID_FAIL,
  FETCH_LESSONS_TEACHER_BY_ID_SUCCESS,
} from "./types";

import axios from "axios";
import {url} from "../helpers/utils";

export const fetchLessonsTeacherDetailed = (id) => async (dispatch, getState) => {
  dispatch({
	type: FETCH_LESSONS_TEACHER_BY_ID,
  })
  try {
	const detailed = await axios.get(`${url}/lessons/teacher/${id}`, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: FETCH_LESSONS_TEACHER_BY_ID_SUCCESS,
	  payload: detailed.data,
	})
  } catch (e) {
	dispatch({
	  type: FETCH_LESSONS_TEACHER_BY_ID_FAIL,
	  error: e,
	})
  }
}

export const deleteChapter = (id) => async (dispatch, getState) => {
  try {
	const detailed = await axios.delete(`${url}/lessons/chapter/delete/${id}`,{
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	console.log(detailed, id)
	dispatch({
	  type: "DELETE_CHAPTER",
	  payload: id,
	})
  } catch (e) {
	dispatch({
	  type: FETCH_LESSONS_TEACHER_BY_ID_FAIL,
	  error: e,
	})
  }
}

export const addChapter = (name, description, lesson) => async (dispatch, getState) => {
  try {
	const detailed = await axios.post(`${url}/lessons/chapter/create/`, {name, description, lesson},{
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }
	})
	dispatch({
	  type: "ADD_CHAPTER",
	  payload: detailed.data,
	})
  } catch (e) {
	dispatch({
	  type: FETCH_LESSONS_TEACHER_BY_ID_FAIL,
	  error: e,
	})
  }
}

export const updateChapter= (lesson,name, description, id) => async (dispatch, getState) => {
  try {
	let detailed = await axios.put(`${url}/lessons/chapter/update/${id}`, {lesson, name, description}, {
	  headers: {
		"Authorization": "JWT " + getState().auth.token.access,
	  }

	})
	dispatch({
	  type: "UPDATE_CHAPTER",
	  payload: {lesson, name, description, id},
	})
  } catch (e) {
	dispatch({
	  type: FETCH_LESSONS_TEACHER_BY_ID_FAIL,
	  error: e,
	})
  }
}