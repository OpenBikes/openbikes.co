import React from 'react';
import { browserHistory, IndexRoute, Route, Router } from 'react-router';

import CityMap from './CityMap.jsx';
import Home from './Home.jsx';
import Layout from './Layout.jsx';

const App = () => (
  <Router history={browserHistory}>
    <Route path="/" component={Layout}>
      <IndexRoute component={Home} />
      <Route path="map" component={CityMap} />
    </Route>
  </Router>
);

export default App;
