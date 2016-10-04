import moment from 'moment'
import Vue from 'vue'
import Vuex from 'vuex'

import { fetchStations } from './api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    city: null,
    lastRefresh: null, // Moment at which time the data was refreshed on the api.openbikes.co server
    center: [],
    stations: [],
    refreshTimer: 60000, // Rate at which the app will check if it's data is obsolete
    expirationDuration: 120000 // Duration after which the data is considered obsolete
  },

  mutations: {
    SET_CURRENT_CITY: (state, city) => {
      if (state.city !== city) state.lastRefresh = null // Force a station refresh on the next fetch
      state.city = city
    },
    SET_LAST_REFRESH: (state, time) => { state.lastRefresh = time },
    SET_MAP_CENTER: (state, center) => { state.center = [center.latitude, center.longitude] },
    SET_STATIONS: (state, stations) => { state.stations = stations }
  },

  actions: {
    FETCH_STATIONS: (context) => {
      // Use a promise so that the caller knows when the stations have been fetched
      return new Promise((resolve, reject) => {
        // Check if a refresh is justifiable or if instead the current data should be used
        const dataHasExpired = moment()
          .subtract(context.state.expirationDuration, 'ms')
          .isBefore(context.state.lastRefresh)
        if (!context.state.lastRefresh || dataHasExpired) {
          fetchStations(context.state.city).then(r => {
            context.commit('SET_LAST_REFRESH', moment(r.update))
            context.commit('SET_MAP_CENTER', r.center)
            context.commit('SET_STATIONS', r.features)
            resolve()
          })
        } else resolve()
      })
    }
  }
})
