/**
 * Created by xlin on 16/03/17.
 */
'use strict';

export const SWITCH_LOADING_LISTINGS = 'SWITCH_LOADING_LISTINGS';

export const SET_LISTINGS = 'SET_LISTINGS';

export const SET_PREV_LISTINGS_URL = 'SET_PREV_LISTINGS_URL';

export const SET_NEXT_LISTINGS_URL = 'SET_NEXT_LISTINGS_URL';


export const switchLoadingListings = (isLoadingListings) => ({
    type: SWITCH_LOADING_LISTINGS,
    isLoadingListings
});

export const setListings = (listings) => ({
    type: SET_LISTINGS,
    listings
});

export const setPrevListingsUrl = (url) => ({
    type: SET_PREV_LISTINGS_URL,
    url
});

export const setNextListingsUrl = (url) => ({
    type: SET_NEXT_LISTINGS_URL,
    url
});