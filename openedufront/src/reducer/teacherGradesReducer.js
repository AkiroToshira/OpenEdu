import {
  FETCH_TEACHER_GRADES,
  FETCH_TEACHER_GRADES_FAIL,
  FETCH_TEACHER_GRADES_SUCCESS
} from "../actions/types";

const defaultState = {
  id: null,
  columns: [],
  group: {},
  loading: true,
  error: null,
}


export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_TEACHER_GRADES:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_TEACHER_GRADES_SUCCESS:
	  return {
		...state,
		loading: false,
		...action.payload
	  }
	case FETCH_TEACHER_GRADES_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		columns: [],
		group: {}
	  }

	case "UPDATE_TEACHER_GRADE":
	  return {
		...state,
		loading: false,
		error: action.error,
		columns: state.columns.map((el, i) => i === action.payload.col ?
			{
			  ...el, grades: state.columns[action.payload.col].grades.map(el =>
				  el.id === action.payload.id
					  ?
					  {...el, value: action.payload.value}
					  : el)
			}
			: el)
	  }
	default:
	  return state;
  }
}