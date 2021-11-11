import axios from 'axios';

import {API_URL} from './constants';

export const isTokenValid = async (token) => {
  const req = {headers: {'x-jwt-key': token}};

  const config = {validateStatus: (status) => status};

  try {
    const res = await axios.post(API_URL + '/validate', req, config);
    return res.status == 200;
  } catch {
    console.log('Is server down?');
  }

  return false;
};
