import React from 'react';
// import logo from '../assets/cetys-logo.jpg';
import './Home.css';

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: '',
    };
  }
  render() {
    return (
      <div id="login-form">
        <div>
          {/* <img className="mt-3" src={logo} id="logo"></img> */}
          <h1>Busqueda</h1>
        </div>
        <form>
          <div className="input-group input-group-lg">
            <input type="text"
              className="form-control rounded-pill"
              placeholder="Describe tu objeto..."
              aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-lg"/>
          </div>
        </form>
      </div>
    );
  }
}

export default Home;
