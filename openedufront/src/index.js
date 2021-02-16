import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {Provider} from "react-redux";
import {store} from "./reducer";
import {BrowserRouter as Router} from "react-router-dom";
import {QueryClient, QueryClientProvider, useQuery} from "react-query";

const queryClient = new QueryClient();

ReactDOM.render(
	<Provider store={store}>
	  <QueryClientProvider client={queryClient}>
		<React.StrictMode>
		  <Router>
			<App/>
		  </Router>
		</React.StrictMode>
	  </QueryClientProvider>
	</Provider>,
	document.getElementById('root')
);
