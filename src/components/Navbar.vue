<template>
  <nav class="blue-grey darken-3" role="navigation">
    <div class="nav-wrapper container">
      <ul class="right hide-on-med-and-down"><Routes></Routes></ul>
      <ul id="mobile-nav" class="side-nav"><Routes></Routes></ul>
      <a href="#" data-activates="mobile-nav" class="button-collapse"><i class="material-icons">menu</i></a>
    </div>
  </nav>
</template>

<script>
import Routes from '../components/Routes.vue';

$(document).ready(() => {
  $('.button-collapse').sideNav();
});

export default {
  components: {
    Routes,
  },
};
</script>
