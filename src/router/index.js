import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import AboutView from '../views/AboutView.vue'
import HomeView from '../views/HomeView.vue'
import MapView from '../views/MapView.vue'
import SearchView from '../views/SearchView.vue'

export default new Router({
  mode: 'history',
  linkActiveClass: 'active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    { path: '/', component: HomeView, name: 'home' },
    { path: '/search', component: SearchView, name: 'search' },
    { path: '/map', component: MapView, name: 'map' },
    { path: '/map/:citySlug', component: MapView, name: 'map' },
    { path: '/about', component: AboutView, name: 'about' }
  ]
})
