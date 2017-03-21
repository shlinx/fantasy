/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import {
    SET_LISTINGS,
    SWITCH_LOADING_LISTINGS,
} from '../actions/index';

const isLoadingListings = (state = false, action) => (
    action.type === SWITCH_LOADING_LISTINGS ? action.isLoadingListings : state
);

const listings = (state = [], action) => (action.type === SET_LISTINGS ? action.listings : state);

const reducers = {
    isLoadingListings,
    listings,
};

export default reducers;