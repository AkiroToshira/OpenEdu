import {
  FETCH_GRADES_LESSONS,
  FETCH_GRADES_LESSONS_FAIL,
  FETCH_GRADES_LESSONS_SUCCESS,
} from "../actions/types";

const defaultState = {
  id: null,
  lessons: [],
  loading: true,
  error: null,
}

export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_GRADES_LESSONS:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_GRADES_LESSONS_SUCCESS:
	  return {
		...state,
		loading: false,
		lessons: [...action.payload]
	  }
	case FETCH_GRADES_LESSONS_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		lessons: [],
	  }
	default:
	  return state;
  }
}

