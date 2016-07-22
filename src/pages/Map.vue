<template>
  <div id="map">Hello</div>
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
  height: 380px;
</style>
