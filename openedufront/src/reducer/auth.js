import {
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
} from "../actions/types";

const token = JSON.parse(localStorage.getItem("user"));

const initialState = token
	? { isLoggedIn: true, token }
	: { isLoggedIn: false, user: null };

export default function (state = initialState, action) {
  const { type, payload } = action;

  switch (type) {
	case LOGIN_SUCCESS:
	  return {
		...state,
		isLoggedIn: true,
		user: payload.user,
	  };
	case LOGIN_FAIL:
	  return {
		...state,
		isLoggedIn: false,
		user: null,
	  };
	case LOGOUT:
	  return {
		...state,
		isLoggedIn: false,
		user: null,
	  };
	default:
	  return state;
  }
}