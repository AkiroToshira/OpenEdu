import axios from 'axios'
import {setUser, setUserLoginError, setUserToken} from "../reducer/userReducer";
import {url} from "../helpers/utils";
import {setProfile} from "../reducer/profileReducer";
import {setError, setErrorAction} from "../reducer/errorReducer";

export const loginUser = (password, username) => {
  return async (dispatch) => {

	// GRAB TOKEN
	const token = await axios.post("http://127.0.0.1:8000/token/", {password, username}).then((res) => {
	  dispatch(setUserToken(res.data))
	  return res
	}).catch((e) => {
	  dispatch(setErrorAction(e))
	})
	if (token) {
	  // GRAB USER ID
	  const user = await axios.get("http://127.0.0.1:8000/user/react-info/", {
		headers: {
		  "Authorization": 'JWT ' + token.data.access,
		}
	  }).then((res) => {
		dispatch(setUser(res.data))
		return res.data
	  }).catch((e) => dispatch(setErrorAction(e)))

	  // GRAB USER INFORMATION

	  await axios.get(`http://127.0.0.1:8000/user/${user.id}`, {
		headers: {
		  Authorization: 'JWT ' + token.data.access,
		  'Content-Type': 'application/json'
		}
	  }).then((res) => {
		dispatch(setProfile(res.data))
	  }).catch((e) => {
		dispatch(setErrorAction(e))
	  })
	}

  }
}