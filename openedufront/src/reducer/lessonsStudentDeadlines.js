import {
  FETCH_DEADLINES_FAIL,
  FETCH_DEADLINES, FETCH_DEADLINES_SUCCESS,
} from "../actions/types";

const defaultState = {
  deadlines: [],
  loading: true,
  error: null,
}


export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_DEADLINES:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_DEADLINES_SUCCESS:
	  return {
		...state,
		loading: false,
		deadlines: action.payload
	  }
	case FETCH_DEADLINES_FAIL:
	  return {
		...state,
		loading: false,
		error: action.error,
		deadlines: {},
	  }
	default:
	  return state;
  }
}