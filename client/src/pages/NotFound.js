import React from 'react';
import 'bulma/css/bulma.min.css';
import icon from '../assets/404.png';

function NotFound() {
  return (
    <section className="hero is-fullheight">
      <div className="hero-body has-text-centered">
        <div className="container">
          <div className="column">
            <img src={icon} width='100px'/>
            <h1 className="title is-1 is-spaced">LA PAGINA NO EXISTE</h1>
          </div>
        </div>
      </div>
    </section>
  );
}

export default NotFound;
