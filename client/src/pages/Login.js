// Libraries
import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';

// Styles
import './Login.css';
import 'bulma/css/bulma.min.css';

// Components
import useAuth from '../utils/auth';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const {authed, login} = useAuth();
  const navigate = useNavigate();

  const onSubmit = async (event) => {
    event.preventDefault();
    await login(username, password);
    navigate('/search');
  };

  useEffect(() => {
    if (authed) {
      navigate('/search');
    }
  }, [authed]);

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
