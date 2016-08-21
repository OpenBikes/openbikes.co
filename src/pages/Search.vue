<template>
  <div class="container">

    <div class="row">
      <div class="col s6 offset-s3">
        <Multiselect :options="cities",
                     :searchable="true",
                     :show-labels="false"
                     placeholder="Search"
                     label="name">
        </Multiselect>
      </div>
    </div>

    <div class="row">
      <div class="col s12 m6 l4" v-for="city in cities">
        <Card :city="city"></Card>
      </div>
    </div>

  </div>
</template>

<script>
import Multiselect from 'vue-multiselect';

import Card from '../components/Card.vue';


export default {
  name: 'Search',
  components: {
    Card,
    Multiselect,
  },
  data: () => ({
    input: '',
    cities: [
      {
        active: true,
        country: 'France',
        latitude: 43.6018906155859,
        longitude: 1.4436077736487,
        name: 'Toulouse',
        predictable: true,
        provider: 'jcdecaux',
        slug: 'toulouse',
      },
      {
        active: true,
        country: 'Belgium',
        latitude: 50.842670192015,
        longitude: 4.36068610685475,
        name: 'Brussels',
        predictable: true,
        provider: 'jcdecaux',
        slug: 'brussels',
      },
      {
        active: true,
        country: 'France',
        latitude: 49.8940298692084,
        longitude: 2.29725010938634,
        name: 'Amiens',
        predictable: true,
        provider: 'jcdecaux',
        slug: 'amiens',
      },
      {
        active: true,
        country: 'France',
        latitude: 49.0368759562153,
        longitude: 2.05919134071038,
        name: 'Cergy',
        predictable: true,
        provider: 'jcdecaux',
        slug: 'cergy',
      },
    ],
  }),
  ready: function ready() {
    // fetch('/api/cities')
    //   .then(response => response.json())
    //   .then(data => { this.cities = data.cities; });
  },
};
</script>

<style scoped lang="sass">
.search-container
  height: 200px;
  width: 300px;

.search-bar
  margin-top: 100px;
</style>
