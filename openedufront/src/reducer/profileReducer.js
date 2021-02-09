const SET_PROFILE = "SET_PROFILE_INFORMATION"
const SET_PROFILE_IMG = "SET_PROFILE_PHOTO"

const defaultState = {
  email: "",
  firstName: "",
  lastName: "",
  profile: {middleName: "", numberPhone: "", creditBookNumber: "", img: ""},
  username: "",
}

export default function profileReducer(state = defaultState, action) {
  switch (action.type) {
	case SET_PROFILE:
	  return {
		...state,
		...action.payload
	  }
	case SET_PROFILE_IMG:
	  return null
	default:
	  return state;
  }
}

export const setProfile = (info) => ({type:SET_PROFILE, payload: info})

