const SET_USER = "SET_USER"
const SET_USER_TOKEN = "SET_TOKEN"
const SET_USER_LOGOUT = "SET_USER_LOGOUT"


const defaultState = {
  id: 0,
  role: '',
  isLogged: false,
  refresh: '',
  token: '',
}

export default function userReducer(state = defaultState, action) {
  switch (action.type) {
	case SET_USER:
	  return {
		...state,
		id: action.payload.id,
		role: action.payload.perm.toLowerCase(),
		isLogged: true
	  }
	case SET_USER_LOGOUT:
	  return {
		...state,
		isLogged: action.payload
	  }
	case SET_USER_TOKEN:
	  return {
		...state,
		token: action.payload.access,
		refresh: action.payload.refresh,
	  }
	default:
	  return state;
  }
}

export const setUser = (user) => ({type: SET_USER, payload: user})
export const setUserToken = (token) => ({type: SET_USER_TOKEN, payload: token})
export const setUserLogout = () => ({type: SET_USER_LOGOUT, payload: false})
