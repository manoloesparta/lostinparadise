import React from 'react';
// import {ReactComponent as Logo} from '../logo192.png';
import logo from '../assets/cetys-logo.jpg';
import './login.css';
import axios from 'axios';
let JWT = '';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e) {
    const value = e.target.value;
    const name = e.target.name;
    this.setState({[name]: value}, () => {
      // console.log(this.state);
    });
  }

  handleSubmit(e) {
    e.preventDefault();
    axios.post('http://localhost:5000/login', this.state)
        .then((response) => {
          JWT = response.data.message['X-Jwt-Key'];
          if (JWT) {
            localStorage.setItem('user_token', JWT);
            console.log('JWT : ' + JWT);
            console.log(response.data.message);
          } else {
            console.log(response.data.message);
          }
          console.log('Status Code ' + response.data.statusCode);
        }).catch((err) => {

        });
  }
  render() {
    return (
      <div id="login-form">
        <div>
          <img className="mt-3 img-fluid" src={logo} id="logo"></img>
        </div>
        <form onSubmit={this.handleSubmit}>
          <div className="input-group input-group-lg">
            <input type="text"
              className="form-control"
              name="username"
              placeholder="Matrícula"
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
