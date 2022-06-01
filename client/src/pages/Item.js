import React from "react";

function Item({ category, foundOn, buildingName, description, icon }) {
  return (
    <div className="card">
      <div className="card-content">
        <div className="media">
          <div className="media-left">
            <figure className="image">
              <img src={icon} alt="placeholder" style={{ width: "100px" }} />
            </figure>
          </div>
          <div className="media-content">
            <p className="is-6">
              <strong>Categoria: </strong>
              {category}
            </p>
            <p className="is-6">
              <strong>Cuando: </strong>
              {foundOn}
            </p>
            <p className="is-6">
              <strong>Donde: </strong>
              {buildingName}
            </p>
            <p className="is-6">
              <strong>Descripcion: </strong>
              {description}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Item;
