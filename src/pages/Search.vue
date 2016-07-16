<template>
  <div id="search">

    <div class="row search-container">
      <div class="center col s12">
        <div class="input-field col s6 offset-s3 search-bar">
          <input v-model="input"
                 v-el:input
                 debounce="200"
                 placeholder="Find your city"
                 type="text"
                 class="validate">
        </div>
      </div>
    </div>

    <div>
      <button @click='increment'>Increment +1</button>
    </div>

    <h3>Count is {{ counterValue }}</h3>

    <div class="container">
      <Grid :items="filteredItems">
      </Grid>
    </div>

  </div>
</template>

<script>
import Grid from '../components/Grid.vue';

import { incrementCounter } from '../vuex/actions';
import { getCount } from '../vuex/getters';

export default {
  name: 'Search',
  components: {
    Grid,
  },
  el: () => '#search',
  data: () => ({
    input: '',
    filteredItems: [
      { name: 'Toulouse' },
      { name: 'Paris' },
      { name: 'Rome' },
      { name: 'London' },
    ],
  }),
  ready: () => {
    // fetch('/api/updates')
    // .then(response => response.json())
    // .then(data => console.log(data));
  },
  vuex: {
    actions: {
      increment: incrementCounter,
    },
    getters: {
      counterValue: getCount,
    },
  },
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
