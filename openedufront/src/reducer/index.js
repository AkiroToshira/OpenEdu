import {combineReducers} from "redux";

import {createStore, applyMiddleware} from "redux";
import {composeWithDevTools} from "redux-devtools-extension";
import thunk from "redux-thunk";
import userReducer from "./userReducer";
import profileReducer from "./profileReducer";
import auth from "./auth";
import message from "./message";

const rootReducer = combineReducers({
  auth,
  message,
})

export const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)))