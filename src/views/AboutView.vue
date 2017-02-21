<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <p>OpenBikes est un projet alimenté par les étudiants en sciences de données et de business intelligence de l'Université Paul Sabatier - Toulouse III</p>
        <p>Les vélos en libre-partage font partie de l’écosystème urbain dans le monde entier. Nous voulons rendre le transport en vélo un jeu d’enfant.</p>
        <p>Notre système est construit avec des outils open-source et l’état de l’art des technologies requises.</p>
      </div>
    </div>
    <div class="row">
      <div class="col offset-s2 s8 m5">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/max_halford.jpg">
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
            <h3>Fondateur</h3>
            <p>OpenBikes est une excellente opportunité pour moi de me parfaire en mathématiques et en informatiques. Je trouve cela intéressant de pouvoir prédire des choses à l’avance. Je prend aussi de plaisir à résoudre les problèmes algorithmiques auxquels nous devons faire face, par exemple la récupération des données en temps réel et la gestion d’une grande base de donnée noSQL.</p>
          </div>
          <div class="card-action" style="padding-bottom: 5px;">
            <div class="row">
              <div class="col s4 center" v-for="logo in teamMembersLogos.max">
                <a :href="logo.url">
                  <i :class="'logo-icon fa fa-3x fa-' + logo.icon" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col offset-s2 s8 offset-m2 m5">
        <div class="card">
          <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="../assets/axel_bellec.jpg">
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
            <h3>Collaborateur</h3>
            <p>Je suis un étudiant en sciences de données qui a une passion pour l’analyse des données et la programmation. Je suis aussi intéressé par la data-visualisation. Je suis fasciné par les langages de programmation tel que R et Python.</p>
          </div>
          <div class="card-action" style="padding-bottom: 5px;">
            <div class="row">
              <div class="col s4 center" v-for="logo in teamMembersLogos.axel">
                <a :href="logo.url">
                  <i :class="'logo-icon fa fa-3x fa-' + logo.icon" aria-hidden="true"></i>
                </a>
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
  name: 'AboutView',
  data: () => ({
    teamMembersLogos: {
      max: [
        { icon: 'home', url: 'http://maxhalford.com/' },
        { icon: 'github', url: 'https://github.com/MaxHalford' },
        { icon: 'linkedin', url: 'https://www.linkedin.com/in/maxhalford' }
      ],
      axel: [
        { icon: 'home', url: 'http://axelbellec.fr/' },
        { icon: 'github', url: 'https://github.com/axelbellec' },
        { icon: 'linkedin', url: 'https://www.linkedin.com/in/axelbellec' }
      ]
    }
  })
}
</script>

<style scoped lang="sass">
@import "../variables.sass"

.logo-icon
  color: $cadet-blue

  &:hover
    color: $sky-blue
</style>
