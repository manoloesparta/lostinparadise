// Libraries
import React, {useEffect} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

// Styles
import './App.css';

// Scripts
import {isTokenValid} from './utils/token';

// Components
import Home from './pages/Home';
import Login from './pages/Login';

function App() {
<<<<<<< HEAD
  useEffect(async () => {
    const currentToken = localStorage.getItem('user_token');
    const logged = await isTokenValid(currentToken);
    console.log(logged);
  }, []);
=======
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
>>>>>>> 2fa97f746f115633daa7c89731cd19e889c35db1

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
