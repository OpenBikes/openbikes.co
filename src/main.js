// Expose jQuery as global `$` and `jQuery`
import 'expose?$!jquery'
import 'expose?jQuery!jquery'

import 'leaflet'
import 'materialize-css'

L.Icon.Default.imagePath = '/static/vendor/leaflet/images'

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

/* eslint-disable no-new */
new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
})
