import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React from 'react';
import { browserHistory, IndexRoute, Route, Router } from 'react-router';

import CityMap from './CityMap.jsx';
import Home from './Home.jsx';
import Layout from './Layout.jsx';

const App = () => (
  <MuiThemeProvider muiTheme={getMuiTheme()}>
    <Router history={browserHistory}>
      <Route path="/" component={Layout}>
        <IndexRoute component={Home} />
        <Route path="cities" component={CityMap} />
      </Route>
    </Router>
  </MuiThemeProvider>
);

export default App;
