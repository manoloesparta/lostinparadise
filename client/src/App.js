import React from 'react';
import './App.css';
import Login from '../src/pages/Login';
import Home from '../src/pages/Home';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path={['/', '/login']}>
            <Login></Login>
          </Route>
          <Route exact path = "/home">
            <Home ></Home>
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
