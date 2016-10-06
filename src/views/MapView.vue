<template>
  <div id="map"></div>
</template>

<script>
import tinycolor from 'tinycolor2'

const getColor = ratio => {
  const hue = 120 + ratio * 80
  const saturation = 100
  const luminosity = 35 + ratio * 60
  const hsl = `hsl(${hue}, ${saturation}%, ${luminosity}%)`
  return `#${tinycolor(hsl).toHex()}`
}

const defineMarkerOptions = (bikes, stands, status) => ({
  radius: 8,
  fillColor: status === 'OPEN' ? getColor(stands / (stands + bikes)) : '#980000',
  fillOpacity: 0.8,
  weight: 2.5,
  color: '#263238',
  opacity: 1
})

export default {
  name: 'MapView',
  data: () => ({
    map: null,
    status: 'loading',
    markers: new Map()
  }),
  mounted: function () {
    // The user has chosen a city
    if (this.$route.params.hasOwnProperty('citySlug')) {
      const citySlug = this.$route.params.citySlug
      // The city the user has chosen if different from the one he chose previously
      if (!this.$store.state.currentCity || citySlug !== this.$store.state.currentCity.slug) {
        this.$store.dispatch('FETCH_CITY', citySlug).then(() => this.setupMap())
      } else this.setupMap()
    // The user has clicked on the "Map tab and chose a city during his session
    } else if (this.$store.state.currentCity) this.setupMap()
    // The user has clicked on the "Map tab but hasn't chosen any city previously
    else {
      console.log('TODO')
    }
    // Fetch the stations, once this is done the map can be setup and the markers can be displayed
    // Refresh the data every 2 minutes
    setInterval(
      () => this.$store.dispatch('FETCH_STATIONS').then(this.displayMarkers()),
      this.$store.state.refreshTimer
    )
    this.status = 'ready'
  },
  methods: {
    setupMap: function () {
      this.map = L.map('map')
      L.tileLayer('https://{s}.tiles.mapbox.com/v4/{mapId}/{z}/{x}/{y}.png?access_token={token}', {
        attribution: '<a href="https://www.mapbox.com/about/maps/" target="_blank">&copy; Mapbox &copy; OpenStreetMap</a>',
        subdomains: ['a', 'b', 'c', 'd'],
        mapId: 'mapbox.outdoors',
        token: 'pk.eyJ1IjoibGVtYXgiLCJhIjoidnNDV1kzNCJ9.iH26jLhEuimYd6vLOO6v1g'
      }).addTo(this.map)
      const center = [
        this.$store.state.currentCity.latitude,
        this.$store.state.currentCity.longitude
      ]
      this.map.setView(center, 13)
      this.$store.dispatch('FETCH_STATIONS').then(() => this.displayMarkers())
    },
    createMarker: function (station) {
      const markerOptions = defineMarkerOptions(
        station.properties.bikes,
        station.properties.stands,
        station.properties.status
      )
      const marker = L.geoJson(station, {
        pointToLayer: (feature, latlng) => L.circleMarker(latlng, markerOptions),
        onEachFeature: (feature, layer) => { layer.bindPopup(feature.properties.address) },
        bikes: station.properties.bikes,
        stands: station.properties.stands,
        status: station.properties.status
      })
      this.markers.set(station.properties.slug, marker)
      marker.addTo(this.map)
    },
    displayMarkers: function () {
      for (const station of this.$store.state.stations) {
        // If the marker is already on the map, only refresh it if something changed
        if (this.markers.has(station.properties.slug)) {
          const marker = this.markers.get(station.properties.slug)
          if (marker.options.bikes !== station.properties.bikes ||
              marker.options.stands !== station.properties.stands ||
              marker.options.status !== station.properties.status) {
            this.map.removeLayer(marker)
            this.createMarker(station)
          }
        } else this.createMarker(station)
      }
    }
  }
}
</script>
