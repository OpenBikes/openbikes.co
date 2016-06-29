<template>
  <footer class="page-footer blue-grey darken-2">
    <div class="container">
      <div class="row">
        <div class="col l10 push-l1 pull-l1">
          <div class="row">
            <div class="col s12 m4">
              <div class="card-panel blue-grey footer-card">
                <div class="row center">
                  <ul>
                    <li v-for="link in leftLinks">
                      <a class="white-text" href="{{ link.url }}">{{ link.label }}</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="col s12 m4">
              <div class="card-panel blue-grey footer-card-logos">
                <div class="row center">
                  <div class="col s4 m12">
                    <i class="fa fa-5x fa-facebook-square white-text" aria-hidden="true"></i>
                  </div>
                  <div class="col s4 m12">
                    <i class="fa fa-5x fa-twitter white-text" aria-hidden="true"></i>
                  </div>
                  <div class="col s4 m12">
                    <i class="fa fa-5x fa-github white-text" aria-hidden="true"></i>
                  </div>
                </div>
              </div>
            </div>
            <div class="col s12 m4">
              <div class="card-panel blue-grey footer-card">
                <div class="row center">
                  <ul>
                    <li v-for="link in rightLinks">
                      <a class="white-text" href="{{ link.url }}">{{ link.label }}</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-copyright">
      <div class="center container">
        © 2016 OpenBikes - contact.openbikes@gmail.com
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data: () => ({
    leftLinks: [
      { label: 'JCDecaux developer', url: 'https://developer.jcdecaux.com/' },
    ],
    rightLinks: [
      { label: 'data.gouv.fr', url: 'https://www.data.gouv.fr/fr/' },
    ],
  }),
};
</script>

<style lang="sass">
.footer-card
  height: 260px;

.footer-card-logos
  @extend .footer-card;

  @media screen and (max-width: 600px)
    height: 110px;
</style>
