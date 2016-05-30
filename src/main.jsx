import injectTapEventPlugin from 'react-tap-event-plugin';

// Needed for onTouchTap
// Check this repo:
// https://github.com/zilverline/react-tap-event-plugin
injectTapEventPlugin();

import './main.scss';

import React from 'react';
import ReactDOM from 'react-dom';

import App from './components/App.jsx';

ReactDOM.render(<App />, document.getElementById('root'));
