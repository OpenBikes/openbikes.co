<template>
  <div id="search">

    <div class="row search-container">
      <div class="center col s12">
        <div class="input-field col s6 offset-s3 search-bar">
          <input v-model="input"
                 debounce="200"
                 placeholder="Find your city"
                 type="text"
                 class="validate">
        </div>
      </div>
    </div>

    <div class="container">
      <Grid :items="cities"
            :query="input">
      </Grid>
    </div>

  </div>
</template>

<script>
import Grid from '../components/Grid.vue';

export default {
  name: 'Search',
  components: {
    Grid,
  },
  el: () => '#search',
  data: () => ({
    input: '',
    cities: [
      { name: 'Toulouse' },
      { name: 'Paris' },
      { name: 'Rome' },
      { name: 'London' },
    ],
  }),
};
</script>

<style scoped>
.search-container {
  height: 300px;
}

.search-bar {
  margin-top: 100px;
}
</style>
