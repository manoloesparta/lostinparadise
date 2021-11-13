import React from 'react';


function Item(props) {
  return (
    <div className="card">
      <div className="card-content">
        <div className="media">
          <div className="media-left">
            <figure className="image">
              <img src={props.icon} alt="Placeholder image"/>
            </figure>
          </div>
          <div className="media-content">
            <p className="is-6">
              <strong>Categoria:</strong> {props.categoria}</p>
            <p className="is-6">
              <strong>Cuando: </strong> {props.cuando}</p>
            <p className="is-6">
              <strong>Donde: </strong> {props.donde}</p>
            <p className="is-6">
              <strong>Descripcion:
              </strong> {props.desc}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Item;
