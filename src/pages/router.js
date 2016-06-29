import Vue from 'vue';
import VueRouter from 'vue-router';

import About from './pages/About';
import Home from './pages/Home';
import CityMap from './pages/Map';
import Search from './pages/Search';

Vue.use(VueRouter);

const router = new VueRouter({
  history: true,
});

router.map({
  '/': {
    name: 'home',
    component: Home,
  },
  '/about': {
    name: 'about',
    component: About,
  },
  '/map': {
    name: 'map',
    component: CityMap,
  },
  '/search': {
    name: 'search',
    component: Search,
  },
});

router.beforeEach(() => {
  window.scrollTo(0, 0);
});

export router
