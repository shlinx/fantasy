/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import React from 'react';
import {connect} from 'react-redux';

import Filters from './filters';
import Results from './results';
import Pagination from './pagination';
import Map from './map';
import {
    switchLoadingListings,
    setListings,
    setCount,
    setPage,
    setNumPages,
    setPrevListingsUrl,
    setNextListingsUrl,
} from '../actions/index';

const EFFECTIVE_QUERIES = [
    'business_type',
    'regionname',
    'keywords',
    'page'
];

class App extends React.Component {
    constructor(props) {
        super(props);
        this.request = null;
    }

    componentWillMount() {
        this.loadListings();
    }

    componentDidUpdate(prevProps) {
        let shouldLoadListings = false;
        for (let query of EFFECTIVE_QUERIES) {
            if(prevProps.location.query[query] !== this.props.location.query[query]) {
                shouldLoadListings = true;
            }
        }
        shouldLoadListings && this.loadListings();
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
                this.props.dispatch(setCount(data.count));
                this.props.dispatch(setPage(data.page));
                this.props.dispatch(setNumPages(data.num_pages));
                this.props.dispatch(switchLoadingListings(false));
                this.props.dispatch(setPrevListingsUrl(data.previous));
                this.props.dispatch(setNextListingsUrl(data.next));
                this.props.dispatch(switchLoadingListings(false));
            }
        });
    }

    render() {
        return (
            <div className={this.props.isLoadingListings ? 'loading' : ''}>
                <div id="filter-container">
                    <Filters location={this.props.location}/>
                </div>
                <div id="results-container">
                    <Results location={this.props.location}/>
                    <Pagination location={this.props.location}/>
                </div>
                <div id="map-container">
                    <Map location={this.props.location}/>
                </div>
            </div>
        );
    }
}

export default connect((state) => ({
    isLoadingListings: state.isLoadingListings
}))(App);