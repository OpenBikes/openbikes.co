import App from './App';
import router from './router';

router.beforeEach(() => {
  window.scrollTo(0, 0);
});

router.start(App, '#app');
