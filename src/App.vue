<template>
  <div class="global-container" id="app">

      <div class="ui labeled icon menu teal">
        <a class="item" v-link="{ path: '/', activeClass: 'active', exact: true }">
          <i class="home icon"></i> Home
        </a>
        <a class="item" v-link="{ path: '/search', activeClass: 'active' }">
          <i class="search icon"></i> Search
        </a>
        <a class="item" v-link="{ path: '/map', activeClass: 'active' }">
          <i class="map icon"></i> Map
        </a>
        <a class="item" v-link="{ path: '/about', activeClass: 'active' }">
          <i class="info icon"></i> About
        </a>
      </div>

    <div class="content-container">
      <router-view></router-view>
    </div>

    <div class="ui blue inverted vertical footer segment">
      <div class="ui center aligned container footer-container">
        <div class="ui three column stackable grid">
          <div class="column">
            <div class="ui inverted teal segment footer-segment">
              <h4 class="ui inverted header">Community</h4>
              <div class="ui inverted link list">
                <a class="item" href="https://www.transifex.com/organization/semantic-org/" target="_blank">Help Translate</a>
                <a class="item" href="https://github.com/Semantic-Org/Semantic-UI/issues" target="_blank">Submit an Issue</a>
                <a class="item" href="https://gitter.im/Semantic-Org/Semantic-UI" target="_blank">Join our Chat</a>
                <a class="item" href="/cla.html" target="_blank">CLA</a>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="ui inverted teal segment footer-segment">
              <h4 class="ui inverted header">Community</h4>
              <div class="ui inverted link list">
                <a class="item" href="https://www.transifex.com/organization/semantic-org/" target="_blank">Help Translate</a>
                <a class="item" href="https://github.com/Semantic-Org/Semantic-UI/issues" target="_blank">Submit an Issue</a>
                <a class="item" href="https://gitter.im/Semantic-Org/Semantic-UI" target="_blank">Join our Chat</a>
                <a class="item" href="/cla.html" target="_blank">CLA</a>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="ui inverted teal segment footer-segment">
              <h4 class="ui inverted header">Community</h4>
              <div class="ui inverted link list">
                <a class="item" href="https://www.transifex.com/organization/semantic-org/" target="_blank">Help Translate</a>
                <a class="item" href="https://github.com/Semantic-Org/Semantic-UI/issues" target="_blank">Submit an Issue</a>
                <a class="item" href="https://gitter.im/Semantic-Org/Semantic-UI" target="_blank">Join our Chat</a>
                <a class="item" href="/cla.html" target="_blank">CLA</a>
              </div>
            </div>
          </div>
      </div>
    </div>

  </div>
</template>

<style lang="scss">
@import './semantic/dist/semantic.min.css';
</style>

<style>
.global-container {
  display: flex;
  min-height: 100%;
  flex-direction: column;
}

.content-container {
  flex: 1;
}

.footer-container {
  padding: 20px;
}

.footer-segment {
  margin: 0 20px;
}
</style>
