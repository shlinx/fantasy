/**
 * Created by xlin on 16/03/17.
 */
'use strict';

import React from 'react';
import { connect } from 'react-redux';

import Filters from './filters';
import Results from './results';
import Map from './map';

class App extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                <Filters/>
                <Results/>
                <Map/>
            </div>
        );
    }
}

export default App;