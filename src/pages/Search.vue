<template>


  <div class="ui centered grid search-container">
    <div id="search-input" class="ui search">
      <div class="ui icon huge input">
        <input class="prompt" type="text" placeholder="Find your city">
        <i class="search icon"></i>
      </div>
      <div class="results"></div>
    </div>
  </div>

  <div class="ui container">
    <div class="ui three stackable cards">

      <a class="ui card" v-link="{ path: '/map' }">
        <div class="content">
          <div class="header">Cute Dog</div>
          <div class="meta">
            <span class="category">Animals</span>
          </div>
          <div class="description">
            <p></p>
          </div>
        </div>
        <div class="extra content">
          <div class="right floated author">
            <img class="ui avatar image" src="/images/avatar/small/matt.jpg"> Matt
          </div>
        </div>
      </a>

    </div>
  </div>
</template>

<script>

export default {};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}

.search-container {
  margin: 70px;
}
</style>
