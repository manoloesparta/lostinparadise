import React from 'react';
import 'bulma/css/bulma.min.css';

function NotFound() {
  return (
    <section className="hero is-fullheight">
      <div className="hero-body has-text-centered">
        <div className="container">
          <div className="column">
            <img src="/404icon.png"/>
            <h1 className="title is-1 is-spaced">404 <br/>La pagina no
            se pudo encontrar!</h1>
          </div>
        </div>
      </div>
    </section>
  );
}

export default NotFound;
