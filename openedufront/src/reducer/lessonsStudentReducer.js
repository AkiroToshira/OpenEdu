import {
  FETCH_LESSONS_STUDENT, FETCH_LESSONS_STUDENT_FAIL, FETCH_LESSONS_STUDENT_SUCCESS
} from "../actions/types";

const defaultState = {
  lessons: [],
  loading: false,
  error: null,
}


export default function(state = defaultState, action) {
	switch(action.type) {
	  case FETCH_LESSONS_STUDENT:
		return {
		  ...state,
		  loading: true,
		  error: null,
		}
	  case FETCH_LESSONS_STUDENT_SUCCESS:
		return {
		  ...state,
		  loading: false,
		  lessons: action.payload,
		}
	  case FETCH_LESSONS_STUDENT_FAIL:
		return {
		  ...state,
		  loading: false,
		  error: action.error,
		  lessons: {},
		}
	  default:
		return state;
	}
}