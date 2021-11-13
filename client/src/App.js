// Libraries
import React from 'react';
// import {BrowserRouter} from 'react-router-dom';
// import {Route, Routes} from 'react-router-dom';
// import {Fragment} from 'react';

// Styles
// import './App.css';

// Scripts
// import {isTokenValid} from './utils/token';

// Components
// import Home from './pages/Home';
// import Login from './pages/Login';
import Search from './pages/search';

function App() {
  // useEffect(async () => {
  //   const currentToken = localStorage.getItem('user_token');
  //   const logged = await isTokenValid(currentToken);
  //   console.log(logged);
  // }, []);

  return (
    <div className="App">
      <Search></Search>
    </div>
  );
}

export default App;
