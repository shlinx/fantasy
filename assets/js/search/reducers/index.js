/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import {SET_LISTINGS} from '../actions'

const listings = (state = [], action) => {
    switch(action.type) {
        case SET_LISTINGS:
            return action.listings;
        default:
            return state;
    }
};

const reducers = {
    listings,
};

export default reducers;