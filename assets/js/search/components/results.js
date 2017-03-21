/**
 * Created by xlin on 20/03/17.
 */
'use strict';

import React from 'react';
import { connect } from 'react-redux';

import Card from './card';

class Results extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                {
                    this.props.listings.map((listing) => (
                        <Card listing={listing} key={listing.pk}/>
                    ))
                }
            </div>
        );
    }
}

export default connect((state) => ({
    listings: state.listings
}))(Results);