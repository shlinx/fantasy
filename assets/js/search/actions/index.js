/**
 * Created by xlin on 16/03/17.
 */
'use strict';

export const SWITCH_LOADING_LISTINGS = 'SWITCH_LOADING_LISTINGS';

export const SET_LISTINGS = 'SET_LISTINGS';

export const SET_COUNT = 'SET_COUNT';

export const SET_NUM_PAGES = 'SET_NUM_PAGES';

export const SET_PAGE = 'SET_PAGE';

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

export const setCount = (count) => ({
    type: SET_COUNT,
    count
});

export const setPage = (page) => ({
    type: SET_PAGE,
    page
});

export const setNumPages = (number) => ({
    type: SET_NUM_PAGES,
    number
});

export const setPrevListingsUrl = (url) => ({
    type: SET_PREV_LISTINGS_URL,
    url
});

export const setNextListingsUrl = (url) => ({
    type: SET_NEXT_LISTINGS_URL,
    url
});