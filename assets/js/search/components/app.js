/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import React from 'react';
import {connect} from 'react-redux';

import Filters from './filters';
import Results from './results';
import Map from './map';
import {
    switchLoadingListings,
    setListings,
    setPrevListingsUrl,
    setNextListingsUrl,
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
                this.props.dispatch(setListings(data.results));
                this.props.dispatch(switchLoadingListings(false));
                this.props.dispatch(setPrevListingsUrl(data.previous));
                this.props.dispatch(setNextListingsUrl(data.next));
            }
        });
    }

    render() {
        return (
            <div>
                <div className="col-sm-12">
                    <Filters location={this.props.location}/>
                </div>
                <div className="col-sm-12">
                    <div className="col-md-6">
                        <Results location={this.props.location}/>
                    </div>
                    <div className="col-md-4">
                        <Map location={this.props.location}/>
                    </div>
                </div>
            </div>
        );
    }
}

export default connect((state) => ({
    isLoadingListings: state.isLoadingListings
}))(App);