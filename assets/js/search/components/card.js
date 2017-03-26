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
                    style={{backgroundImage: `url('${listing.main_image.file}')`}}
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