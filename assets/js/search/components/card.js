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
            <div>
                <a
                    href=""
                    className="grid-item-container"
                    style={{backgroundImage: `url('${listing.fields.main_image}')`}}
                >
                    <header>
                        <h4>{listing.fields.name}</h4>
                    </header>
                    <div className="summary">
                        <p>
                            {listing.fields.listing_summary}
                        </p>
                    </div>
                </a>

            </div>
        );
    }
}

export default Card;