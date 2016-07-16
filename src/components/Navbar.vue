<template>
  <nav class="blue-grey lighten" role="navigation">
    <div class="nav-wrapper container">
      <ul class="right hide-on-med-and-down">
        <Routes></Routes>
      </ul>
      <ul id="mobile-nav" class="side-nav">
        <Routes></Routes>
      </ul>
      <a href="#" data-activates="mobile-nav" id="navbar-burger"><i class="mdi-navigation-menu"></i></a>
    </div>
  </nav>
</template>

<script>
import Routes from '../components/Routes.vue';

// import $ from 'jquery';
// $(document).ready(() => {
//   $('.navbar-burger').sideNav();
// });

export default {
  components: {
    Routes,
  },
};
</script>
