import React from 'react';
import { browserHistory } from 'react-router';

import AppBar from 'material-ui/AppBar';
import { Tabs, Tab } from 'material-ui/Tabs';
import FontIcon from 'material-ui/FontIcon';

const styles = {
  tabs: {
    width: 500,
    'margin-top': -13,
    'margin-right': -8,
  },
};

function clickTab(tab) {
  browserHistory.push(tab.props.path);
}

const tabs = (
  <Tabs style={styles.tabs}>
    <Tab
      label="Home"
      path="/"
      icon={<FontIcon className="fa fa-home" />}
      onActive={clickTab}
    />
    <Tab
      label="Cities"
      path="/cities"
      icon={<FontIcon className="fa fa-bicycle" />}
      onActive={clickTab}
    />
  </Tabs>
);

const Navbar = () => (
  <AppBar title="OpenBikes" iconElementRight={tabs} />
);

export default Navbar;
