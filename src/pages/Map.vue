<template>
  <div id="map"></div>
</template>

<script>
import moment from 'moment';
import tinycolor from 'tinycolor2';

import { fetchJson } from '../util';

const getColor = ratio => {
  const hue = 120 + ratio * 80;
  const saturation = 100;
  const luminosity = 35 + ratio * 60;
  const hsl = `hsl(${hue}, ${saturation}%, ${luminosity}%)`;
  return `#${tinycolor(hsl).toHex()}`;
};

const defineMarkerOptions = (bikes, stands, status) => ({
  radius: 8,
  fillColor: status === 'OPEN' ? getColor(stands / (stands + bikes)) : '#980000',
  fillOpacity: 0.8,
  weight: 2.5,
  color: '#263238',
  opacity: 1,
});

export default {
  name: 'Map',
  data: () => ({
    map: null,
    status: 'loading',
    lastUpdate: null,
    stations: [],
    markers: new Map(),
  }),
  computed: {
    citySlug: function() { return this.$route.query.city; },
  },
  watch: {
    stations: function(newStations) {
      for (const station of newStations) {
        // If the marker is already on the map, only refresh it if it has changed in any way
        if (this.markers.has(station.properties.slug)) {
          const marker = this.markers.get(station.properties.slug);
          if (marker.options.bikes !== station.properties.bikes ||
              marker.options.stands !== station.properties.stands ||
              marker.options.status !== station.properties.status) {
            this.map.removeLayer(marker);
            this.createMarker(station);
          }
        } else this.createMarker(station);
      }
    },
  },
  ready: function() {
    this.setupMap();
    this.fetchStations();
    this.status = 'ready';
    setInterval(this.fetchStations, 60000);
  },
  methods: {
    fetchStations: function() {
      fetchJson('GET', `/api/geojson/${this.citySlug}`)
      .then(city => {
        this.map.setView([city.center.latitude, city.center.longitude], 13);
        this.lastUpdate = moment(city.update);
        this.stations = city.features;
      })
      .catch(() => { this.status = 'failure'; });
    },
    setupMap: function() {
      this.map = L.map('map');
      L.tileLayer('https://{s}.tiles.mapbox.com/v4/{mapId}/{z}/{x}/{y}.png?access_token={token}', {
        attribution: '<a href="https://www.mapbox.com/about/maps/" target="_blank">&copy; Mapbox &copy; OpenStreetMap</a>',
        subdomains: ['a', 'b', 'c', 'd'],
        mapId: 'mapbox.outdoors',
        token: 'pk.eyJ1IjoibGVtYXgiLCJhIjoidnNDV1kzNCJ9.iH26jLhEuimYd6vLOO6v1g',
      }).addTo(this.map);
    },
    createMarker: function(station) {
      const markerOptions = defineMarkerOptions(
        station.properties.bikes,
        station.properties.stands,
        station.properties.status
      );
      const marker = L.geoJson(station, {
        pointToLayer: (feature, latlng) => L.circleMarker(latlng, markerOptions),
        onEachFeature: (feature, layer) => { layer.bindPopup(feature.properties.address); },
        bikes: station.properties.bikes,
        stands: station.properties.stands,
        status: station.properties.status,
      });
      this.markers.set(station.properties.slug, marker);
      marker.addTo(this.map);
    },
  },
};
</script>

<style scoped lang="sass">
#map
  height: 600px;
</style>
