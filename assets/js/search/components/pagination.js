/**
 * Created by xlin on 30/03/17.
 */
'use strict';

import {connect} from 'react-redux';
import React from 'react';
import {browserHistory} from 'react-router';

let PageButton = ({location, page, goToPage, label, isLoadingListings}) => {
    return (
        <li className={"page-number" + ( page === goToPage ? " active" : "")}>
            <button
                    disabled={isLoadingListings}
                    onClick={() => {
                        let query = Object.assign({}, location.query, {page: goToPage});
                        if(goToPage === 1) {
                            delete query.page
                        }
                        browserHistory.push({
                            pathname: location.pathname,
                            query: query
                        });
                    }}>{label}</button>
        </li>
    )
};

PageButton = connect((state) => ({
    isLoadingListings: state.isLoadingListings,
    page: state.page,
}))(PageButton);

export const Pagination = ({numPages, page, location}) => {
    return (
        <div className="results-pagination-container">
            <ul className="results-pagination">
                {page > 1 ? <PageButton location={location} goToPage={page - 1} label="&larr;"/> : ''}
                {page > 2 ? <PageButton location={location} goToPage="1" label="1"/> : ''}
                {page > 3 ? <li className="page-number gap">&hellip;</li> : ''}
                {page > 1 ? <PageButton location={location} goToPage={page - 1} label={page - 1}/> : ''}
                <PageButton location={location} goToPage={page} label={page}/>
                {page < numPages ? <PageButton location={location} goToPage={page + 1} label={page + 1}/> : ''}
                {page < numPages - 2 ? <li className="page-number gap">&hellip;</li>  : ''}
                {page < numPages - 1 ? <PageButton location={location} goToPage={numPages} label={numPages}/> : ''}
                {page < numPages ? <PageButton location={location} goToPage={page + 1} label="&rarr;"/> : ''}
            </ul>
        </div>
    );
};

const mapStateToProps = (state) => ({
    page: state.page,
    numPages: state.numPages,
    isLoadingListings: state.isLoadingListings,
});

export default connect(mapStateToProps)(Pagination);