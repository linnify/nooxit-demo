import React from 'react'
import {Link} from "react-router-dom";
import './Nav.css';

function Nav() {
  return (
    <nav className={'Nav'}>
      <Link className={'Nav-link'} to="/">Users</Link>
      <Link className={'Nav-link'} to="/members">Members</Link>
    </nav>
  )
}

export default Nav;
