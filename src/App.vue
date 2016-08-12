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
import About from './pages/About';
import CityMap from './pages/Map';
import Foot from './components/Footer';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Search from './pages/Search';


export default {
  name: 'App',
  components: { About, CityMap, Foot, Home, Navbar, Search },
};
</script>

<style lang="sass">
@import "./style.sass"

.app
  display: flex;
  min-height: 100vh;
  flex-direction: column;

.page
  flex: 1 0 auto;
</style>
