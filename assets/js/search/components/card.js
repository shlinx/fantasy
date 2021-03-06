/**
 * Created by xlin on 20/03/17.
 */
'use strict';

import React from 'react';
import {connect} from 'react-redux';

class Card extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        let listing = this.props.listing;
        return (
            <div className="col-sm-12 col-md-6 card">
                <a
                    href={listing.url}
                    className="grid-item-container"
                    style={{backgroundImage: `url('${listing.main_image ? listing.main_image.small : ''}')`}}
                >
                    <header>
                        <h4>{listing.name}</h4>
                    </header>
                    <div className="summary">
                        <p>
                            {listing.listing_summary}
                        </p>
                    </div>
                </a>

            </div>
        );
    }
}

export default Card;