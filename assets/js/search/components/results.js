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
                Here are the results!
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
            </div>
        );
    }
}

export default Results;