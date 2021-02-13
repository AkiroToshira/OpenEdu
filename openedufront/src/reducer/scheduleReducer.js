import {FETCH_SCHEDULE, FETCH_SCHEDULE_SUCCESS, FETCH_SCHEDULE_FAIL} from "../actions/types";


const defaultState = {
  days: {},
  loading: true,
  error: null,
}

export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_SCHEDULE:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_SCHEDULE_SUCCESS:
	  return {
		...state,
		loading: false,
		days: action.payload,
	  }
	case FETCH_SCHEDULE_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		days: {}
	  }
	default:
	  return state;
  }
}

