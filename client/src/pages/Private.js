// Libraries
import React from 'react';
import {Navigate, Outlet} from 'react-router-dom';

// Utils
import useAuth from '../utils/auth';

function Private() {
  const {authed} = useAuth();

  return authed ? <Outlet/> : <Navigate to='/login'/>;
}

export default Private;
