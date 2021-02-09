const initState = {
  error: null
};

export function errorReducer(state = initState, action){
  const { error } = action;

  if(error){
	return {
	  error: error
	}
  }

  return state;
}

export const SET_ERROR = "SET_ERROR";

export const setErrorAction = (error) => ({type: SET_ERROR, error: error})