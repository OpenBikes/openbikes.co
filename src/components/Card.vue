<template>
  <div class="card blue-grey darken-1">
    <div class="card-content white-text">
      <span class="card-title">{{ city.name }}</span>
      <p>I am a very simple card. I am good at containing small bits of information.
      I am convenient because I require little markup to use effectively.</p>
    </div>
    <div class="card-action">
      <a v-link="{ path: mapLink }">Go to map</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    city: {
      type: Object,
      required: true,
    },
  },
  computed: {
    mapLink: function() { return `map?city=${this.city.slug}`; },
  },
};
</script>
