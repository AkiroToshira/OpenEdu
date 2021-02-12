import {
  FETCH_LESSONS_STUDENT,
  FETCH_LESSONS_STUDENT_BY_ID, FETCH_LESSONS_STUDENT_BY_ID_FAIL,
  FETCH_LESSONS_STUDENT_BY_ID_SUCCESS,
  FETCH_LESSONS_STUDENT_FAIL,
  FETCH_LESSONS_STUDENT_SUCCESS
} from "../actions/types";

const defaultState = {
  detailed:{},
  loading: true,
  error: null,
}

export default function(state = defaultState, action) {
  switch(action.type) {
	case FETCH_LESSONS_STUDENT_BY_ID:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_LESSONS_STUDENT_BY_ID_SUCCESS:
	  return {
		...state,
		loading: false,
		detailed: action.payload
	  }
	case FETCH_LESSONS_STUDENT_BY_ID_FAIL:
	  return {
		...state,
		loading: false,
		error: action.error,
		detailed: {},
	  }
	default:
	  return state;
  }
}