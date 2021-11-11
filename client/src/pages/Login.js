// Libraries
import axios from 'axios';
import React, {useState} from 'react';
import Swal from 'sweetalert2';

// Styles
import './login.css';
import 'bulma/css/bulma.min.css';

// Scripts
import {API_URL} from '../utils/constants';

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
      const config = {validateStatus: (status) => status};
      const res = await axios.post(API_URL + '/login', req, config);

      if (res.status == 201) {
        const token = res.data.data['x-jwt-key'];
        localStorage.setItem('user_token', token);
        console.log(`Token: ${token}`);
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: '¿Trataste con tu matricula y contraseña de Mi Campus?',
          confirmButtonColor: '#edbd00',
        });
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
    <div className="container is-flex is-justify-content-center
         is-align-items-center" style={{height: '100vh'}}>
      <div className="columns" style={{width: '100vw'}}>
        <div className="column">
          <h1 className="title is-1 is-spaced">Cosas <br/>Perdidas</h1>
          <h2 className="subtitle">by CETYS</h2>
        </div>
        <div className="column">
          <form className="box">
            <div className="field">
              <label className="label">Matricula</label>
              <div className="control">
                <input className="input"
                  type="email"
                  placeholder="e.g. t030046"
                  required onChange={handleUsername}/>
              </div>
            </div>

            <div className="field">
              <label className="label">Contraseña</label>
              <div className="control">
                <input className="input"
                  type="password"
                  placeholder="********"
                  required onChange={handlePassword}/>
              </div>
            </div>
            <hr/>
            <button className="button is-primary"
              id="signin"
              type="button"
              onClick={onSubmit}>Sign in</button>
          </form>
        </div>
      </div>
    </div>
  );
}


export default Login;
