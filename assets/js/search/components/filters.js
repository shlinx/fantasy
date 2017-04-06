/**
 * Created by xlin on 20/03/17.
 */
'use strict';

import React from 'react';
import {connect} from 'react-redux';

class KeywordsFilter extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <input type="search" placeholder="公园、海滩、博物馆..."/>
        );
    }
}

class TypeFilter extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <select>
                <option value>全部</option>
            </select>
        );
    }
}

class RegionFilter extends React.Component {
    constructor(props) {
        super(props);
    }

    handleChange() {

    }

    render() {
        return (
            <select onChange={this.handleChange.bind(this)}>
                <option value>全部</option>
            </select>
        );
    }
}

class Filters extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <form>
                    <RegionFilter location={this.props.location}/>
                    <TypeFilter location={this.props.location}/>
                    <KeywordsFilter location={this.props.location}/>
                </form>
            </div>
        );
    }
}

export default Filters;