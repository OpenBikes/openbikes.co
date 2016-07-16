<template>
  <footer class="page-footer blue-grey darken-2">
    <div class="container">
      <div class="row">
        <div class="col s12 m4">
          <div class="card-panel blue-grey footer-card">
            <div class="row center">
              <ul>
                <li class="col s4 m12" v-for="link in leftLinks">
                  <a class="white-text" href="{{ link.url }}">{{ link.label }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col s12 m4">
          <div class="card-panel blue-grey footer-card">
            <div class="row center">
              <ul>
                <li class="col s4 m12" v-for="link in rightLinks">
                  <a class="white-text" href="{{ link.url }}">{{ link.label }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col s12 m4">
          <div class="card-panel blue-grey footer-card">
            <div class="row center">
              <div class="col s4 m12 card-logo">
                <i class="fa fa-5x fa-facebook-square white-text" aria-hidden="true"></i>
              </div>
              <div class="col s4 m12 card-logo">
                <i class="fa fa-5x fa-twitter white-text" aria-hidden="true"></i>
              </div>
              <div class="col s4 m12 card-logo">
                <i class="fa fa-5x fa-github white-text" aria-hidden="true"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-copyright">
      <div class="center container">
        contact.openbikes@gmail.com
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data: () => ({
    leftLinks: [
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
      { label: 'JCDecaux', url: 'https://developer.jcdecaux.com/' },
    ],
    rightLinks: [
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
    ],
  }),
};
</script>

<style scoped lang="sass">
.footer-card
  height: 260px;

  @media screen and (max-width: 600px)
    height: 130px;

.card-logo
  margin-top: 3px;

  @media screen and (max-width: 600px)
    margin-top: 10px;
</style>
