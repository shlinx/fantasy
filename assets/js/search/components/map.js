/**
 * Created by xlin on 20/03/17.
 */
'use strict';

import React from 'react';
import ReactDOM from 'react-dom';
import {connect} from 'react-redux';
import {browserHistory} from 'react-router';

class Map extends React.Component {
    constructor(props) {
        super(props);
        this.map = null;
        this.markerSize = new google.maps.Size(35, 45);
        this.markers = {};
        this.activeListing = null;
        this.infoWindow = new google.maps.InfoWindow();
    }

    render() {
        return (
            <div>
                <div ref="map" className="map">Loading map...</div>
            </div>
        );
    }

    componentDidMount() {
        this.loadMap();
        this.renderListingsMarkers();
    }

    componentDidUpdate(prevProps) {
        if (prevProps.listings !== this.props.listings) {
            this.renderListingsMarkers();
        }
    }

    loadMap() {
        const mapNode = ReactDOM.findDOMNode(this.refs.map);
        this.map = new google.maps.Map(mapNode, {
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.TERRAIN,
            center: new google.maps.LatLng({lat: -41.1491663, lng: 173.6747732}),
            zoom: 6,
        });

        google.maps.event.addListener(this.map, 'dragend', this.pushBounds.bind(this));
        google.maps.event.addListener(this.map, 'zoom_changed', this.pushBounds.bind(this));
    }

    renderListingsMarkers() {
        for (let identifier in this.markers) {
            if (this.markers.hasOwnProperty(identifier)) {
                this.markers[identifier].setMap(null);
            }
        }
        this.markers = {};
        this.activeListing = null;
        this.infoWindow.close();

        const listings = this.props.listings;

        if (!listings.length) {
            return;
        }
        for (let listing of listings) {
            this.addMarker(listing);
        }
    }

    addMarker(listing) {
        let lat = parseFloat(listing.lat),
            lng = parseFloat(listing.lng);

        if (!lat || !lng) {
            return;
        }

        let lagLng = new google.maps.LatLng({lat: lat, lng: lng}),
            markerOptions = {
                map: this.map,
                animation: google.maps.Animation.DROP,
                position: lagLng,
                icon: {
                    scaledSize: this.markerSize
                }
            };
        if (listing.hasOwnProperty('icon')) {
            markerOptions.icon.url = listing.icon;
        }
        let marker = new google.maps.Marker(markerOptions);
        marker.addListener('click', () => this.setActiveListing(listing));
        this.markers[listing.identifier] = marker;
    };

    openInfoWindow(listing) {
        const infoWindow = this.infoWindow;
        let marker = this.markers[listing.identifier],
            image = listing.image ? listing.image : '',
            content = `
                <div>${listing.name}</div>
            `;
        infoWindow.setContent(content);
        this.infoWindow.open(this.map, marker);
    }

    setActiveListing(listing) {
        this.clearActiveListing();
        let marker = this.markers[listing.identifier];
        marker.setAnimation(google.maps.Animation.BOUNCE);
        this.openInfoWindow(listing);
        this.activeListing = listing;
    }

    clearActiveListing() {
        if (!this.activeListing) return;
        let marker = this.markers[this.activeListing.identifier];
        marker.setAnimation(null);
        this.activeListing = null;
        this.infoWindow.close();
    }

    pushBounds() {
        let boundsData = this.map.getBounds().toJSON(),
            newQuery = Object.assign({}, this.props.location.query, boundsData);

        browserHistory.push({
            pathname: this.props.location.pathname,
            query: newQuery
        });
    }
}

export default connect((state) => ({
    listings: state.listings
}))(Map);