import {combineReducers} from "redux";

import {createStore, applyMiddleware} from "redux";
import {composeWithDevTools} from "redux-devtools-extension";
import thunk from "redux-thunk";

import auth from "./auth";
import message from "./message";
import profile from './profileReducer'
import news from './newsReducer'
import schedule from './scheduleReducer'
import lessonsStudent from './lessonsStudentReducer'
import lessonsTeacher from './lessonsTeacherReducer'
import lessonsStudentById from './lessonsStudentById'
import deadlines from './lessonsStudentDeadlines'
import lessonsTeacherById from './lessonsTeacherById'

const rootReducer = combineReducers({
  profile,
  auth,
  message,
  news,
  schedule,
  lessonsStudent,
  lessonsStudentById,
  lessonsTeacher,
  lessonsTeacherById,
  deadlines,
})

export const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)))