import React from 'react';
import { Link } from 'react-router';

const Navbar = () => (
  <ul>
    <li><Link to="/">Home</Link></li>
    <li><Link to="/map">Map</Link></li>
  </ul>
);

export default Navbar;
