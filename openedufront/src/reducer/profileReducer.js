import {FETCH_PROFILE, FETCH_PROFILE_FAIL, FETCH_PROFILE_SUCCESS} from "../actions/types";

const defaultState = {
  email: "",
  firstName: "",
  lastName: "",
  profile: {
	middleName: "",
	numberPhone: "",
	creditBookNumber: "",
	img: "",
  },
  username: "",
  role: "",
  id: null,
  loading: true,
  error: null
}

export default function (state = defaultState, action) {
  switch (action.type) {
	case FETCH_PROFILE:
	  return {
		...state,
		loading: true,
		error: null,
	  }
	case FETCH_PROFILE_SUCCESS:
	  return {
		...state,
		loading: false,
		...action.payload
	  }
	case FETCH_PROFILE_FAIL:
	  return {
		...state,
		loading: true,
		error: action.error,
		profile: {}
	  }
	default:
	  return state;
  }
}

