import React from 'react';
import { browserHistory, IndexRoute, Route, Router } from 'react-router';

import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import Layout from './Layout.jsx';

import Home from './home/Home.jsx';
import Search from './search/Search.jsx';

const App = () => (
  <MuiThemeProvider muiTheme={getMuiTheme()}>
    <Router history={browserHistory}>
      <Route path="/" component={Layout}>
        <IndexRoute component={Home} />
        <Route path="search" component={Search} />
      </Route>
    </Router>
  </MuiThemeProvider>
);

export default App;
