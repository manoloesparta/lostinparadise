import React from 'react';
import {useState} from 'react';
import Item from './item';
import './search.css';
import 'bulma/css/bulma.min.css';
import * as data from './mockdata.json';

function Search() {
  const postsPerPage =4;
  const items = data.default.items;
  const willSmith = Math.ceil(items.length/postsPerPage);
  const [currentPage, setCurrentPage] = useState(1);
  const pages = [];
  for (let index = 1; index <= willSmith; index++) {
    if (index == currentPage) {
      pages.push(<li><a className="pagination-link is-current">
        {index}</a></li>);
    } else {
      pages.push(<li><a className="pagination-link">{index}</a></li>);
    }
  }

  console.log(setCurrentPage);

  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const currentPosts = items.slice(indexOfFirstPost, indexOfLastPost);

  // console.log(items);
  console.log(currentPosts);
  // console.log(currentPage);
  // console.log(currentPosts);


  return (
    <div className="container is-max-desktop
    is-flex is-justify-content-center is-align-items-center"
    style={{height: '100%'}}>
      <div className="columns" style={{width: '100vw'}}>
        <div className="column">
          <h1 className="title is-1">¿Perdiste Algo?</h1>
          <input className="input is-large is-focused"
            type="text"
            placeholder="Cargador, camisa, chamarra ..."/>
          <div className="items">
            <Item icon={'https://bulma.io/images/placeholders/96x96.png'}
              categoria={'bruh'}
              donde={'ayer'}
              cuando={'manana'}
              desc={'maybe idk yes'}></Item>
            <Item icon={'https://bulma.io/images/placeholders/96x96.png'}
              categoria={'JBM'}
              donde={'MIZAEL'}
              cuando={'EVERYDAY'}
              desc={'anda medio monke'}></Item>
            <Item icon={'https://bulma.io/images/placeholders/96x96.png'}
              categoria={'ima quit everyday'}
              donde={'could never be'}
              cuando={'daniel at work'}
              desc={'juampy sus'}></Item>
            <Item icon={'https://bulma.io/images/placeholders/96x96.png'}
              categoria={'this could look bad '}
              donde={'nah bruh '}
              cuando={'huh'}
              desc={'mifjajs'}></Item>
          </div>
          <nav className="pagination">
            <a className="pagination-next logout">Log Out</a>
            <ul className="pagination-list">
              {pages}
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}


export default Search;

