const axios = require("axios");
const {setErrorAction} = require("../reducer/errorReducer");
const {store} = require("../reducer");

const server = axios.create({
  baseURL: 'http://127.0.0.1:8000',
})

class API {

  constructor() {
	this.token = store.getState().user.token
  }

  dispatch(action) {
	store.dispatch(action)
  }

  getHeaderWithToken = () => {
	return {
	  headers: {
		"Authorization": 'JWT ' + this.token,
		'Content-Type': 'application/json'
	  }
	}
  }

  setError(e) {
	console.warn(e)
	this.dispatch(setErrorAction(e))
  }

  async getNewsDataAndSet() {
	// this.dispatch(setUserAction(result.data.user))
	return await server.get('/news/', this.getHeaderWithToken())
		.catch((e) => this.setError(e))
  }


}

export default new API()