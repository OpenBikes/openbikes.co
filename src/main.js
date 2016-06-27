import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App';

import About from './pages/About';
import Home from './pages/Home';
import Map from './pages/Map';
import Search from './pages/Search';

Vue.use(VueRouter);

const router = new VueRouter({
  history: true,
});

router.map({
  '/': {
    component: Home,
  },
  '/about': {
    component: About,
  },
  '/map': {
    component: Map,
  },
  '/search': {
    component: Search,
  },
});

router.start(App, 'app');
