<template>
  <div class="container">
    <!-- <div class="row">
      <div class="col s6 offset-s3">
        <Multiselect :options="cities"
                     :searchable="true"
                     :show-labels="false"
                     placeholder="Search"
                     label="name">
        </Multiselect>
      </div>
    </div> -->
    <div class="row">
      <div class="col s12 m6 l4" v-for="city in cities">
        <Card :city="city"></Card>
      </div>
    </div>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
import Card from '../components/Card.vue'

export default {
  name: 'SearchView',
  components: {
    Card,
    Multiselect
  },
  data: () => ({
    input: '',
    cities: []
  }),
  mounted: function () {
    this.$store.dispatch('FETCH_CITIES').then(() => {
      this.cities = this.$store.state.cities
    })
  }
}
</script>

<style scoped lang="sass">
.search-container
  height: 200px
  width: 300px

.search-bar
  margin-top: 100px
</style>
