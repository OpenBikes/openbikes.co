<template>
  <div id="map"></div>
</template>

<script>
import moment from 'moment';
import tinycolor from 'tinycolor2';

const getColor = ratio => {
  const hue = 120 + ratio * 80;
  const saturation = 100;
  const luminosity = 35 + ratio * 60;
  const hsl = `hsl(${hue}, ${saturation}%, ${luminosity}%)`;
  return `#${tinycolor(hsl).toHex()}`;
};

const getMarkerOptions = (bikes, stands, status) => {
  const fillRatio = stands / (stands + bikes);
  return {
    radius: 8,
    fillColor: status === 'OPEN' ? getColor(fillRatio) : '#980000',
    fillOpacity: 0.8,
    weight: 2.5,
    color: '#263238',
    opacity: 1,
  };
};

export default {
  name: 'Map',
  data: () => ({
    map: null,
    lastUpdate: null,
    stations: [],
    markers: {},
  }),
  computed: {
    citySlug: function() { return this.$route.query.city; },
  },
  watch: {
    stations: function(newStations) {
      for (const station of newStations) {
        const markerOptions = getMarkerOptions(
          station.properties.bikes,
          station.properties.stands,
          station.properties.status
        );
        L.geoJson(station, {
          pointToLayer: (feature, latlng) => L.circleMarker(latlng, markerOptions),
          onEachFeature: (feature, layer) => {
            layer.bindPopup(feature.properties.address);
          },
        }).addTo(this.map);
      }
    },
  },
  ready: function() {
    this.setupMap();
    this.fetchStations();
  },
  methods: {
    fetchStations: function() {
      fetch(`/api/geojson/${this.citySlug}`)
      .then(response => response.json())
      .then(data => {
        this.map.setView([data.center.latitude, data.center.longitude], 13);
        this.lastUpdate = moment(data.update);
        this.stations = data.features;
      });
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
  },
};
</script>

<style scoped lang="sass">
#map
  height: 600px;
</style>
