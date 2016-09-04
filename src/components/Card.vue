<template>
  <div class="card blue-grey darken-1">
    <div class="card-image waves-effect waves-block waves-light">
        <img :src="'static/img/cityMapBackground/'+city.slug+'_'+city.country+'.png'">
    </div>
    <div class="card-content white-text">
      <span class="card-title activator">{{ city.name }}</span>
    </div>
    <div class="card-action">
      <a v-link="{ path: mapLink }">Go to map</a>
    </div>
    <div class="card-reveal">
      <span class="card-title grey-text text-darken-4">{{ city.name }}<i class="material-icons right">close</i></span>
      <p>Active : {{ city.active }}</p>
      <p>Provider : {{ city.provider }}</p>
      <p>Predictable : {{ city.predictable }}</p>
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
    imgPath: function() {
      return `static/img/cityMapBackground/${this.city.slug}_${this.city.country}.png`;
    },
  },
};
</script>

