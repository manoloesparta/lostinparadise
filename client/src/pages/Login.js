import React from 'react';
// import {ReactComponent as Logo} from '../logo192.png';
import logo from '../assets/cetys-logo.jpg';
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
    this.setState({[name]: value}, () => {
      console.log(this.state);
    });
  }

  handleSubmit(e) {
    e.preventDefault();
    console.log(this.state);
    console.log('hello');
  }
  render() {
    return (
      <div id="login-form">
        <div>
          <img className="mt-3" src={logo} id="logo"></img>
        </div>
        <form onSubmit={this.handleSubmit}>
          <div className="input-group input-group-lg">
            <span className="input-group-text" id="basic-addon1">T0</span>
            <input type="text"
              className="form-control"
              name="matricula"
              placeholder="Matrícula"
              aria-describedby="basic-addon1"
              required onChange={this.handleChange} />
          </div>
          <div className="input-group input-group-lg">
            <input type="password"
              className="form-control"
              name="password"
              placeholder="Contraseña"
              required onChange={this.handleChange}/>
          </div>
          <div className="buttonContainer mt-3">
            <button type="submit"
              className="btn btn-warning btn-lg"
              onSubmit={this.handleSubmit}>
            Iniciar sesión</button>
          </div>
        </form>
      </div>
    );
  }
}


export default Login;
