import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Login from "./pages/login/Login";

ReactDOM.render(
	<Router>
	  <React.StrictMode>
		<Switch>
		  <Route exact path={'/'}>
			<Login/>
		  </Route>
		  <Route path={"/news"}>
			<App/>
		  </Route>

		</Switch>
	  </React.StrictMode>
	</Router>,
	document.getElementById('root')
);
