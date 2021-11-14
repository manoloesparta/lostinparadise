import React from 'react';


function Item({categoria, cuando, donde, desc, icon}) {
  return (
    <div className="card">
      <div className="card-content">
        <div className="media">
          <div className="media-left">
            <figure className="image">
              <img src={icon} alt="Placeholder image"/>
            </figure>
          </div>
          <div className="media-content">
            <p className="is-6"><strong>Categoria: </strong>{categoria}</p>
            <p className="is-6"><strong>Cuando: </strong>{cuando}</p>
            <p className="is-6"><strong>Donde: </strong>{donde}</p>
            <p className="is-6"><strong>Descripcion: </strong>{desc}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Item;
