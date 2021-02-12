import {FETCH_LESSONS_TEACHER, FETCH_LESSONS_TEACHER_SUCCESS, FETCH_LESSONS_TEACHER_FAIL} from "../actions/types";

const defaultState = {

}

export default function(state = defaultState, action) {
  switch(action.type) {
	case FETCH_LESSONS_TEACHER:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_LESSONS_TEACHER_SUCCESS:
	  return {
		...state,
		loading: false,
		lessons: action.payload,
	  }
	case FETCH_LESSONS_TEACHER_FAIL:
	  return {
		...state,
		loading: false,
		error: action.error,
		lessons: {}
	  }
	default:
	  return state;
  }
}