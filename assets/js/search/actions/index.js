/**
 * Created by xlin on 16/03/17.
 */
'use strict';

export const SET_LISTINGS = 'SET_LISTINGS';

export const SWITCH_LOADING_LISTINGS = 'SWITCH_LOADING_LISTINGS';

export const setListings = (listings) => ({
    type: SET_LISTINGS,
    listings
});

export const switchLoadingListings = (isLoadingListings) => ({
    type: SWITCH_LOADING_LISTINGS,
    isLoadingListings
});