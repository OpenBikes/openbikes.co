import React from 'react';
import { browserHistory } from 'react-router';

import AppBar from 'material-ui/AppBar';
import { Tabs, Tab } from 'material-ui/Tabs';
import FontIcon from 'material-ui/FontIcon';

const styles = {
  tabs: {
    width: 500,
    marginRight: -24,
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
      path="/search"
      icon={<FontIcon className="fa fa-bicycle" />}
      onActive={clickTab}
    />
    <Tab
      label="Map"
      path="/map"
      icon={<FontIcon className="fa fa-map" />}
      onActive={clickTab}
    />
  </Tabs>
);

const Navbar = () => (
  <AppBar
    title="OpenBikes"
    children={tabs}
  />
);

export default Navbar;
