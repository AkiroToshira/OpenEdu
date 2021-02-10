import {combineReducers} from "redux";

import {createStore, applyMiddleware} from "redux";
import {composeWithDevTools} from "redux-devtools-extension";
import thunk from "redux-thunk";

import auth from "./auth";
import message from "./message";
import profile from './profileReducer'
import news from './newsReducer'

const rootReducer = combineReducers({
  profile,
  auth,
  message,
  news,
})

export const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)))