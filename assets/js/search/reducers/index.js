/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import {
    SWITCH_LOADING_LISTINGS,
    SET_LISTINGS,
    SET_PREV_LISTINGS_URL,
    SET_NEXT_LISTINGS_URL,
} from '../actions/index';

const isLoadingListings = (state = false, action) => (
    action.type === SWITCH_LOADING_LISTINGS ? action.isLoadingListings : state
);

const listings = (state = [], action) => (action.type === SET_LISTINGS ? action.listings : state);

const prevListingsUrl = (state = '', action) => (action.type === SET_PREV_LISTINGS_URL ? action.url : state);

const nextListingsUrl = (state = '', action) => (action.type === SET_NEXT_LISTINGS_URL ? action.url : state);

const reducers = {
    isLoadingListings,
    listings,
    prevListingsUrl,
    nextListingsUrl,
};

export default reducers;