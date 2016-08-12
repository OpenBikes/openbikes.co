<template>
  <footer class="page-footer blue-grey darken-2">
    <div class="container">
      <div class="row">
        <div class="col s12 m4">
          <div class="card-panel blue-grey footer-card">
            <div class="row center">
              <ul>
                <li class="col s6 m12" v-for="link in leftLinks">
                  <a class="" href="{{ link.url }}">{{ link.label }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col s12 m4">
          <div class="card-panel blue-grey footer-card">
            <div class="row center">
              <ul>
                <li class="col s6 m12" v-for="link in rightLinks">
                  <a class="" href="{{ link.url }}">{{ link.label }}</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col s12 m4">
          <div class="card-panel blue-grey footer-card">
            <div class="row center">
              <div class="col s3 m6 card-logo" v-for="logo in logos">
                <a href="{{ logo.url }}">
                  <i class="fa fa-4x fa-{{ logo.icon }}" aria-hidden="true"></i>
                </a>
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
    ],
    rightLinks: [
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
    ],
    logos: [
      { icon: 'facebook-square', url: 'https://www.facebook.com/OpenBikesNotJustBiking/' },
      { icon: 'twitter', url: 'https://twitter.com/openbikes_' },
      { icon: 'book', url: 'http://docs.openbikes.apiary.io/' },
      { icon: 'github', url: 'https://github.com/OpenBikes' },
    ],
  }),
};
</script>

<style scoped lang="sass">
.page-footer
  margin-top: 0;

.footer-card
  height: 200px;

  @media screen and (max-width: 600px)
    height: 130px;

.card-logo
  margin-top: 10px;
  padding-bottom: 16px;

  @media screen and (max-width: 600px)
    margin-top: 14px;
</style>
