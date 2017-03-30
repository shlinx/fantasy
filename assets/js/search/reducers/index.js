/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import {
    SWITCH_LOADING_LISTINGS,
    SET_LISTINGS,
    SET_COUNT,
    SET_PAGE,
    SET_NUM_PAGES,
    SET_PREV_LISTINGS_URL,
    SET_NEXT_LISTINGS_URL,
} from '../actions/index';

const isLoadingListings = (state = false, action) => (
    action.type === SWITCH_LOADING_LISTINGS ? action.isLoadingListings : state
);

const listings = (state = [], action) => (action.type === SET_LISTINGS ? action.listings : state);

const count = (state = 0, action) => (action.type === SET_COUNT ? action.count : state);

const page = (state = 0, action) => (action.type === SET_PAGE ? action.page : state);

const numPages = (state = 0, action) => (action.type === SET_NUM_PAGES ? action.number : state);

const prevListingsUrl = (state = '', action) => (action.type === SET_PREV_LISTINGS_URL ? action.url : state);

const nextListingsUrl = (state = '', action) => (action.type === SET_NEXT_LISTINGS_URL ? action.url : state);

const reducers = {
    isLoadingListings,
    listings,
    count,
    page,
    numPages,
    prevListingsUrl,
    nextListingsUrl,
};

export default reducers;