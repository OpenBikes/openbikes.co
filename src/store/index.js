import moment from 'moment'
import Vue from 'vue'
import Vuex from 'vuex'

import { fetchCity, fetchStations } from './api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentCity: null, // The last city the user chose during his session
    cities: [], // Array containing metadata for each city
    lastRefresh: null, // Moment at which time the data was refreshed on the api.openbikes.co server
    stations: [],
    refreshTimer: 60000, // Rate at which the app will check if it's data is obsolete
    expirationDuration: 120000 // Duration after which the data is considered obsolete
  },

  mutations: {
    SET_CURRENT_CITY: (state, city) => { state.currentCity = city },
    SET_LAST_REFRESH: (state, time) => { state.lastRefresh = time },
    SET_STATIONS: (state, stations) => { state.stations = stations }
  },

  actions: {
    FETCH_CITY: (context, citySlug) => {
      return new Promise((resolve, reject) => {
        fetchCity(citySlug).then(r => {
          context.commit('SET_LAST_REFRESH', null)
          context.commit('SET_CURRENT_CITY', r[0])
          resolve()
        })
      })
    },
    FETCH_STATIONS: (context) => {
      // Use a promise so that the caller knows when the stations have been fetched
      return new Promise((resolve, reject) => {
        // Check if a refresh is justifiable or if instead the current data should be used
        const dataHasExpired = moment()
          .subtract(context.state.expirationDuration, 'ms')
          .isBefore(context.state.lastRefresh)
        if (!context.state.lastRefresh || dataHasExpired) {
          fetchStations(context.state.currentCity.slug).then(r => {
            context.commit('SET_LAST_REFRESH', moment(r.update))
            context.commit('SET_STATIONS', r.features)
            resolve()
          })
        } else resolve()
      })
    }
  }
})
