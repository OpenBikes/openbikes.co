<template>
  <div id="map">
      <p>Hello</p>
  </div>
</template>

<script>
export default {
  name: 'Map',
  data: () => ({
    map: null,
  }),
  ready: () => {
    this.map = L.map('map').setView([51.505, -0.09], 13);
  },
};
</script>

<style scoped lang="sass">
#map
  height: 180px;
</style>
