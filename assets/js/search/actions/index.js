/**
 * Created by xlin on 16/03/17.
 */
'use strict';

export const SET_LISTINGS = 'SET_LISTINGS';

export const setListings = (listings) => ({
    type: SET_LISTINGS,
    listings
});