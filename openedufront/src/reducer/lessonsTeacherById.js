import {
  FETCH_LESSONS_TEACHER_BY_ID,
  FETCH_LESSONS_TEACHER_BY_ID_SUCCESS,
  FETCH_LESSONS_TEACHER_BY_ID_FAIL,

} from "../actions/types";

const defaultState = {
  detailed: {},
  loading: true,
  error: null,
}

export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_LESSONS_TEACHER_BY_ID:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_LESSONS_TEACHER_BY_ID_SUCCESS:
	  return {
		...state,
		loading: false,
		detailed: action.payload
	  }
	case FETCH_LESSONS_TEACHER_BY_ID_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		detailed: {},
	  }

	case "ADD_CHAPTER": {
	  return {
		...state,
		loading: false,
		error: null,
		detailed: {
		  ...state.detailed,
		  chapters: [
		  	...state.detailed.chapters,
			action.payload
		  ]
		}
	  }
	}
	case "DELETE_CHAPTER": {
	  return {
		...state,
		loading: false,
		error: null,
		detailed: {
		  ...state.detailed,
		  chapters: state.detailed.chapters.filter(el => el.id !== action.payload)
		}
	  }
	}
	case "UPDATE_CHAPTER": {
	  return {
		...state,
		loading: false,
		error: null,
		detailed: {
		  ...state.detailed,
		  chapters: state.detailed.chapters.map(
			  (content, i) => content.id === action.payload.id ? action.payload
				  : content
		  )
		}
	  }
	}

	default:
	  return state;
  }
}