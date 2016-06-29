<template>
  <div class="app">
    <Navbar></Navbar>
    <div class="page">
      <router-view></router-view>
    </div>
    <Foot v-if="$route.name !== 'map'"></Foot>
  </div>
</template>

<script>
import Navbar from './components/Navbar';
import Foot from './components/Footer';

import About from './pages/About';
import Home from './pages/Home';
import CityMap from './pages/Map';
import Search from './pages/Search';

export default {
  name: 'App',
  components: { About, Foot, Home, CityMap, Navbar, Search },
};
</script>

<style>
.app {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.page {
  flex: 1 0 auto;
}
</style>
