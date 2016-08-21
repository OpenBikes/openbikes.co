// Expose jQuery as global `$` and `jQuery`
import 'expose?$!jquery';
import 'expose?jQuery!jquery';

import 'leaflet';
import 'materialize-css';

L.Icon.Default.imagePath = '/static/vendor/leaflet/images';

import App from './App';
import router from './router';

router.beforeEach(() => { window.scrollTo(0, 0); });
router.start(App, '#app');
