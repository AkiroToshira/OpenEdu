import {FETCH_NEWS, FETCH_NEWS_SUCCESS, FETCH_NEWS_FAIL} from "../actions/types";


const defaultState = {
  data: {
	mainNews: {},
	smallNews: [],
  },
  loading: true,
  error: null,
}

export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_NEWS:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_NEWS_SUCCESS:
	  return {
		...state,
		loading: false,
		data: action.payload,
	  }
	case FETCH_NEWS_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		data: {}
	  }
	default:
	  return state;
  }
}

