<template>
<div>
  <div class="container">
    <div class="row">
      <div class="col offset-s2 s8 offset-m1 m4">
        <div class="card">
          <div class="card-image">
            <img src="../img/max_halford.jpg">
            <span class="card-title">Max Halford</span>
          </div>
          <div class="card-content">
            <p>I am a very simple card. I am good at containing small bits of information.
            I am convenient because I require little markup to use effectively.</p>
          </div>
          <div class="card-action" style="padding-bottom: 5px;">
            <div class="row">
              <div class="col s4 center" v-for="logo in teamMembersLogos.max">
                <a href="{{ logo.url }}" style="color: #455a64;">
                  <i class="fa fa-3x fa-{{ logo.icon }}" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col offset-s2 s8 offset-m2 m4">
        <div class="card">
          <div class="card-image">
            <img src="../img/axel_bellec.jpg">
            <span class="card-title">Axel Bellec</span>
          </div>
          <div class="card-content">
            <p>I am a very simple card. I am good at containing small bits of information.
            I am convenient because I require little markup to use effectively.</p>
          </div>
          <div class="card-action" style="padding-bottom: 5px;">
            <div class="row">
              <div class="col s4 center" v-for="logo in teamMembersLogos.axel">
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
    teamMembersLogos: {
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
