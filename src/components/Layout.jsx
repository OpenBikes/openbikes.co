import React from 'react';

import Navbar from './Navbar.jsx';

const styles = {
  main: {
    width: '100%',
    height: '100%',
  },
};

const Layout = props => (
  <div>
    <Navbar />
    <main style={styles.main}>
      {props.children}
    </main>
  </div>
);

Layout.propTypes = {
  children: React.PropTypes.node,
};

export default Layout;
