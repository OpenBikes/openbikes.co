// Expose jQuery as global `$` and `jQuery`
import 'expose?$!jquery';
import 'expose?jQuery!jquery';

import '../static/vendor/js/materialize.min.js';
import '../static/vendor/leaflet/leaflet.js';

import App from './App';
import router from './router';

router.beforeEach(() => {
  window.scrollTo(0, 0);
});

router.start(App, '#app');
