// Libraries
import React from 'react';
import axios from 'axios';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

// Styles
import './App.css';

// Components
import Home from './pages/Home';
import Login from './pages/Login';

const API_URL = 'http://localhost:5000';

function App() {
  const currentToken = localStorage.getItem('user_token');

  const isTokenValid = async (token) => {
    const req = {headers: {'x-jwt-key': token}};

    try {
      const config = {validateStatus: (status) => status};
      const res = await axios.post(API_URL + '/validate', req, config);
      return res.status == 200;
    } catch {
      console.log('Is server down?');
    }

    return false;
  };

  const logged = isTokenValid(currentToken);
  console.log(logged);

  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path = "/home">
            <Home ></Home>
          </Route>
          <Route exact path={['/', '/login']}>
            <Login></Login>
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
