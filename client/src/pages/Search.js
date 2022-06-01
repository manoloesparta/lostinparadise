// Libraries
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import Swal from "sweetalert2";

// Components
import Item from "./Item";
import useAuth from "../utils/auth";
import { iconSelector } from "../utils/icon";

// Custom styles
import "bulma/css/bulma.min.css";
import "./Search.css";

const API_URL = "http://localhost:5000";

function Search() {
  const ITEMS_PER_PAGE = 4;

  const [query, setQuery] = useState("default query string");
  const [items, setItems] = useState([]);
  useEffect(async () => {
    const body = {
      method: "POST",
      body: JSON.stringify({ query: query }),
      headers: { "x-jwt-key": localStorage.getItem("user_token") },
    };
    try {
      const response = await fetch(API_URL + "/search", body);
      if (response.status == 200) {
        const json = await response.json();
        setItems(json.data.items);
      }
    } catch {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Algo fallo, intentalo mas tarde",
        confirmButtonColor: "#edbd00",
      });
    }
  }, [query]);

  const numberOfPages = Math.ceil(items.length / ITEMS_PER_PAGE);

  const [currentPage, setCurrentPage] = useState(0);
  const [itemsShown, setItemsShown] = useState([]);

  useEffect(() => {
    const start = currentPage * ITEMS_PER_PAGE;
    const end = currentPage * ITEMS_PER_PAGE + ITEMS_PER_PAGE;
    const slice = items.slice(start, end);
    setItemsShown(slice);
  }, [currentPage, items, query]);

  const { logout } = useAuth();
  const navigate = useNavigate();

  const logoutHandler = () => {
    logout();
    navigate("/login");
  };

  const queryHandler = (event) => {
    if (event.key == "Enter") {
      setQuery(event.target.value);
    }
  };

  const updateCurrentItems = (index) => {
    if (index == currentPage) {
      return (
        <li key={index}>
          <a className="pagination-link is-current">{index + 1}</a>
        </li>
      );
    }
    return (
      <li key={index}>
        <a
          className="pagination-link"
          onClick={() => {
            setCurrentPage(index);
          }}
        >
          {index + 1}
        </a>
      </li>
    );
  };

  return (
    <div
      className="container is-max-desktop
    is-flex is-justify-content-center is-align-items-center"
      style={{ height: "100%" }}
    >
      <div className="columns" style={{ width: "100vw" }}>
        <div className="column">
          <h1 className="title is-1">¿Perdiste Algo?</h1>
          <input
            className="input is-large is-focused"
            type="text"
            onKeyUp={queryHandler}
            placeholder="Cargador, camisa, chamarra ..."
          />
          <div className="items">
            {itemsShown.map((item, index) => (
              <Item
                key={index}
                icon={iconSelector(item.category)}
                category={item.category}
                buildingName={item.buildingName}
                foundOn={item.foundOn}
                description={item.description}
              />
            ))}
          </div>
          <nav className="pagination">
            <a className="pagination-next logout" onClick={logoutHandler}>
              Log Out
            </a>
            <ul className="pagination-list">
              {[...Array(numberOfPages).keys()].map(updateCurrentItems)}
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}

export default Search;
