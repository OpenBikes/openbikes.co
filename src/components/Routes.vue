<template>
  <div>
    <li v-link-active>
      <a class="waves-effect" v-link="{ path: '/', activeClass: 'active', exact: true }">
        <i class="material-icons left">home</i>Home
      </a>
    </li>
    <li v-link-active>
      <a class="waves-effect" v-link="{ path: '/search', activeClass: 'active' }">
        <i class="material-icons left">search</i>Search
      </a>
    </li>
    <li v-link-active>
      <a class="waves-effect" v-link="{ path: '/map', activeClass: 'active' }">
        <i class="material-icons left">map</i>Map
      </a>
    </li>
    <li v-link-active>
      <a class="waves-effect" v-link="{ path: '/about', activeClass: 'active' }">
        <i class="material-icons left">info_outline</i>About
      </a>
    </li>
  <div>
</template>

<script>
export default {};
</script>
