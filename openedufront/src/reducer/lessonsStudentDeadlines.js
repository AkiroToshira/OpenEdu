import {
  FETCH_DEADLINES_FAIL,
  FETCH_DEADLINES, FETCH_DEADLINES_SUCCESS, ADD_DEADLINES,
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
		deadlines: [],
	  }

	case ADD_DEADLINES:
	  return {
	    ...state,
		loading: false,
		error: null,
		deadlines: [...state.deadlines, action.payload]
	  }
	case "UPDATE_DEADLINES": {
	  return {
	    ...state,
		loading: false,
		error: null,
		deadlines: state.deadlines.map(
			(content, i) => content.id === action.payload.id ? action.payload
				: content
		)
	  }
	}
	case "DELETE_DEADLINES": {
	  return {
	    ...state,
		loading: false,
		error: null,
		deadlines: state.deadlines.filter(el => el.id !== action.payload)
	  }
	}
	default:
	  return state;
  }
}