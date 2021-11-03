/* eslint-disable */
import React, {Fragment, useState} from 'react';
import logo from '../assets/cetys-logo.jpg';
import './login.css';
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';


export const LogIn = ({validateUser, error}) => {
  const [details, setDetails] = useState({username: '', password: ''});

  const submitHandler = e => {
    e.preventDefault();
    validateUser(details);
  }

  return (
    <Fragment>
      <div id="login-form">
        <div>
          <img className="mt-3 img-fluid" src={logo} id="logo"></img>
        </div>
        <form onSubmit={submitHandler}>
          <div className="input-group input-group-lg">
            <input type="text"
              className="form-control"
              name="username"
              placeholder="Matrícula"
              onChange={e => setDetails({...details, username: e.target.value})} value={details.username} />
          </div>
          <div className="input-group input-group-lg">
            <input type="password"
              className="form-control"
              name="password"
              placeholder="Contraseña"
              onChange={e => setDetails({...details, password: e.target.value})} value={details.password}/>
          </div>
          <div className="buttonContainer mt-3">
            <button type="submit"
              className="btn btn-warning btn-lg">
            Iniciar sesión</button>
          </div>
        </form>
      </div>
    </Fragment>
  )
}


