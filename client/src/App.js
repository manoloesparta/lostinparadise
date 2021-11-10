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
  useEffect(async () => {
    const currentToken = localStorage.getItem('user_token');
    const logged = await isTokenValid(currentToken);
    console.log(logged);
  }, []);

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
