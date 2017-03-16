/**
 * Created by xlin on 26/02/17.
 */
'use strict';

import '../../scss/search.scss'

import React from 'react';
import ReactDOM from 'react-dom';
import {browserHistory, Router, Route, Link} from 'react-router';
console.log(browserHistory);
import {createStore, combineReducers} from 'redux';
import {Provider} from 'react-redux';
import {syncHistoryWithStore, routerReducer} from 'react-router-redux';

import App from './components/app';
import reducers from './reducers';

const store = createStore(
    combineReducers({
        ...reducers,
        routing: routerReducer
    })
);

const history = syncHistoryWithStore(browserHistory, store);

ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <Route path={window.location.pathname} component={App}/>
        </Router>
    </Provider>,
    document.getElementById('app')
);