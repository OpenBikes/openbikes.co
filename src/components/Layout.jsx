import React from 'react';

import Navbar from './Navbar.jsx';

const Layout = props => (
  <div>
    <Navbar />
    <main>
      {props.children}
    </main>
  </div>
);

Layout.propTypes = {
  children: React.PropTypes.node,
};

export default Layout;