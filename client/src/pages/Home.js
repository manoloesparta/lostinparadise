import React from 'react';
import logo from '../assets/cetys-logo.jpg';

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
          <img className="mt-3" src={logo} id="logo"></img>
        </div>
        <form onSubmit={this.handleSubmit}>
        </form>
      </div>
    );
  }
}

export default Home;
