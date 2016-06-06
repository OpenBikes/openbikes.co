import React from 'react';

import L from 'leaflet';

const styles = {
  map: {
    width: '100%',
    height: '100%',
  },
};

const Map = React.createClass({

  componentDidMount: () => {
    this.lat = 51.505;
    this.lon = -0.09;
    this.zoom = 13;

    const m = L.map('map').setView([this.lat, this.lon], this.zoom);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(m);
  },

  render: () => (
    <div id="map" style={styles.map} />
  ),

});

export default Map;
