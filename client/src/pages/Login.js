// Libraries
import axios from 'axios';
import React, {useState} from 'react';

// Styles
import './login.css';
import 'bootstrap/dist/css/bootstrap.css';
import logo from '../assets/cetys-logo.jpg';

const API_URL = 'http://localhost:5000';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const onSubmit = async (event) => {
    event.preventDefault();

    const req = {
      'username': username,
      'password': password,
    };

    try {
      const res = await axios.post(API_URL + '/login', req);

      if (res.status == 201) {
        const token = res.data.data['x-jwt-key'];
        localStorage.setItem('user_token', token);
        console.log(`Token: ${token}`);
      } else {
        console.log('Incorrect username or password');
      }
    } catch {
      console.log('Is server down?');
    }
  };

  const handlePassword = (event) => {
    setPassword(event.target.value);
  };

  const handleUsername = (event) => {
    setUsername(event.target.value);
  };

  return (
    <div id="login-form">
      <div>
        <img className="mt-3 img-fluid" src={logo} id="logo"></img>
      </div>
      <form>
        <div className="input-group input-group-lg">
          <input type="text"
            className="form-control"
            name="username"
            placeholder="Matrícula"
            required onChange={handleUsername}/>
        </div>
        <div className="input-group input-group-lg">
          <input type="password"
            className="form-control"
            name="password"
            placeholder="Contraseña"
            required onChange={handlePassword}/>
        </div>
        <div className="buttonContainer mt-3">
          <button type="submit"
            className="btn btn-warning btn-lg"
            onClick={onSubmit}>
          Iniciar sesión</button>
        </div>
      </form>
    </div>
  );
}


export default Login;
