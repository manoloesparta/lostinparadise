import React from 'react';
// import {ReactComponent as Logo} from '../logo192.png';
import logo from '../cetys.png';
import './login.css';
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
    };
  }

  handleChange(e) {
    // const {name, value} = e.target;
    // this.setState({[name]: value});
    console.log(e.target.value);
  }

  handleSubmit(e) {

  }
  render() {
    return (
      <div id="login-form">
        <div>
          <img src={logo} id="logo"></img>
        </div>
        <div>
          <form onSubmit={this.handleSubmit}>
            <input type='matricula'
              name='matricula'
              placeholder='matricula'
              required onChange={this.handleChange} />
            <input type='password'
              name='password'
              placeholder='contraseña'
              required onChange={this.handleChange} />
            <button onSubmit={this.handleSubmit}> PROCEDER </button>
          </form>
        </div>
      </div>
    );
  }
}


export default Login;
