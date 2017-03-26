/**
 * Created by xlin on 20/03/17.
 */
'use strict';

import React from 'react';
import {connect} from 'react-redux';

import Card from './card';

class Results extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                {
                    (() => {
                        if (this.props.listings.length) {
                            return this.props.listings.map((listing) => (
                                <Card listing={listing} key={listing.unique_id}/>
                            ))
                        } else {
                            return (
                                <h4>呀，还没有符合条件的信息。您可以试一试改变搜索条件。</h4>
                            )
                        }
                    })()
                }
            </div>
        );
    }
}

export default connect((state) => ({
    listings: state.listings
}))(Results);