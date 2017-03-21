/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import React from 'react';
import { connect } from 'react-redux';

import Filters from './filters';
import Results from './results';
import Map from './map';
import {
    switchLoadingListings,
    setListings,
} from '../actions/index';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.request = null;
    }

    componentWillMount() {
        this.loadListings();
    }

    loadListings() {
        if (this.request) this.request.abort();

        let queryString = $.param(this.props.location.query);
        this.request = $.ajax({
            url: '/api/l/?' + queryString,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => this.props.dispatch(switchLoadingListings(true)),
            success: (data) => {
                this.props.dispatch(setListings(data));
                this.props.dispatch(switchLoadingListings(false));
            }
        });
    }

    render() {
        return (
            <div>
                <Filters/>
                <Results/>
                <Map/>
            </div>
        );
    }
}

export default connect((state) => ({
    isLoadingListings: state.isLoadingListings
}))(App);