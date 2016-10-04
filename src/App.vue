<template>
  <div id="app">
    <Navbar></Navbar>
    <transition name="fade" mode="out-in">
      <router-view class="view"></router-view>
    </transition>
    <Foot v-if="$route.name !== 'map'"></Foot>
  </div>
</template>

<script>
import Foot from './components/Footer'
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Foot, Navbar
  }
}
</script>

<style lang="sass">
@import "./main.sass"

#app
  display: flex;
  min-height: 100vh;
  flex-direction: column;

.fade-enter-active, .fade-leave-active
  transition all .2s ease

.fade-enter, .fade-leave-active
  opacity 0

.view
  flex: 1 0 auto;
</style>
