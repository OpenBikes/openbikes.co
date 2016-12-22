<template>
  <div class="card blue-grey darken-1">
    <div class="card-image waves-effect waves-block waves-light">
      <router-link :to="linkToMap">
        <img :src="pathToPlaceholder">
      </router-link>
    </div>
    <div class="card-content white-text">
      <span class="card-title activator">{{ city.name }}</span>
    </div>
    <div class="card-reveal">
      <span class="card-title grey-text text-darken-4">{{ city.name }}
        <i class="material-icons right">close</i>
      </span>
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
      required: true
    }
  },
  computed: {
    linkToMap: function () { return `map/${this.city.slug}` },
    pathToPlaceholder: function () { return require(`../assets/city_placeholders/${this.city.slug}.png`) }
  }
}
</script>

