<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: 'Map',
  data: () => ({
    map: null,
  }),
  ready: function ready() {
    this.map = L.map('map');
    L.tileLayer('https://{s}.tiles.mapbox.com/v4/{mapId}/{z}/{x}/{y}.png?access_token={token}', {
      attribution: '<a href="https://www.mapbox.com/about/maps/" target="_blank">&copy; Mapbox &copy; OpenStreetMap</a>',
      subdomains: ['a', 'b', 'c', 'd'],
      mapId: 'mapbox.outdoors',
      token: 'pk.eyJ1IjoibGVtYXgiLCJhIjoidnNDV1kzNCJ9.iH26jLhEuimYd6vLOO6v1g',
    }).addTo(this.map);
    this.map.setView([51.505, -0.09], 13);
  },
};
</script>

<style scoped lang="sass">
#map
  height: 500px;
</style>
