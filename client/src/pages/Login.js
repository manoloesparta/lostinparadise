import React from 'react';
// import {ReactComponent as Logo} from '../logo192.png';
import logo from '../cetys_logo.jpg';
import './login.css';
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      matricula: '',
      password: '',
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e) {
    const name = e.target.name;
    const value = e.target.value;
    this.setState({[name]: value});
    console.log(this.state);
  }

  handleSubmit(e) {
    e.preventDefault();
    console.log(this.state);
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
            <br/>
            <input type='password'
              name='password'
              placeholder='contraseña'
              required onChange={this.handleChange} />
            <br/>
            <button onSubmit={this.handleSubmit}> Iniciar Sesion </button>
          </form>
        </div>
      </div>
    );
  }
}


export default Login;
