<template>
<div>
  <div class="container">
    <div class="row">
      <div class="col offset-s2 s8 m5">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../img/max_halford.jpg">
          </div>
          <div class="card-content center">
            <span class="card-title activator">
              Max Halford
            </span>
          </div>
          <div class="card-reveal">
            <span class="card-title">
              <i class="material-icons left">close</i> Max Halford
            </span>
            <p>Here is some more information about this product that is only revealed once clicked on.</p>
          </div>
          <div class="card-action" style="padding-bottom: 5px;">
            <div class="row">
              <div class="col s4 center" v-for="logo in teamMembersLinks.max">
                <a href="{{ logo.url }}" style="color: #455a64;">
                  <i class="fa fa-3x fa-{{ logo.icon }}" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col offset-s2 s8 offset-m2 m5">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../img/axel_bellec.jpg">
          </div>
          <div class="card-content center">
            <span class="card-title activator">
              Axel Bellec
            </span>
          </div>
          <div class="card-reveal">
            <span class="card-title">
              <i class="material-icons left">close</i> Axel Bellec
            </span>
            <p>Here is some more information about this product that is only revealed once clicked on.</p>
          </div>
          <div class="card-action" style="padding-bottom: 5px;">
            <div class="row">
              <div class="col s4 center" v-for="logo in teamMembersLinks.axel">
                <a href="{{ logo.url }}" style="color: #455a64;">
                  <i class="fa fa-3x fa-{{ logo.icon }}" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'About',
  data: () => ({
    teamMembersLinks: {
      max: [
        { icon: 'home', url: 'http://maxhalford.com/' },
        { icon: 'github', url: 'https://github.com/MaxHalford' },
        { icon: 'linkedin', url: 'https://www.linkedin.com/in/maxhalford' },
      ],
      axel: [
        { icon: 'home', url: 'http://axelbellec.fr/' },
        { icon: 'github', url: 'https://github.com/axelbellec' },
        { icon: 'linkedin', url: 'https://www.linkedin.com/in/axelbellec' },
      ],
    },
  }),
};
</script>

<style scoped lang="sass">
.card-title
  font-size: 30px;
  font-weight: 400;
</style>

