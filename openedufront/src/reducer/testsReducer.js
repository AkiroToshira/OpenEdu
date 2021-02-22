import {
  FETCH_TESTS,
  FETCH_TESTS_FAIL,
  FETCH_TESTS_SUCCESS
} from "../actions/types";

const defaultState = {
  tests: [],
  questions: {},
  loading: true,
  error: null,
}

export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_TESTS:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_TESTS_SUCCESS:
	  return {
		...state,
		loading: false,
		tests: action.payload,
	  }
	case FETCH_TESTS_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		tests: [],
		questions: {}
	  }

	case "FETCH_TESTS_QUESTIONS":
	  return {
	    ...state,
		loading: false,
		error: null,
		questions: action.payload
	  }

	default:
	  return state;
  }
}