<template>
  <div class="row">
    <div class="col s12 m6 l4" v-for="item in filteredItems">
      <Card></Card>
    </div>
  </div>
</template>

<script>
import Card from '../components/Card.vue';

export default {
  components: {
    Card,
  },
  props: {
    items: {
      type: Array,
      required: true,
    },
    query: {
      type: String,
      required: true,
    },
  },
  data: () => ({
    filteredItems: [
      { name: 'Toulouse' },
      { name: 'Paris' },
      { name: 'Rome' },
      { name: 'London' },
    ],
  }),
};
</script>
