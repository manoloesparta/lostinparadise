// Libraries
import React, {useEffect, useState} from 'react';
import 'bulma/css/bulma.min.css';

// Components
import Item from './Item';

// Custom styles
import './Search.css';

const data = [
  {
    'categoria': 'fermin',
    'cuando': '2020-01-24',
    'donde': 'asudsuas',
    'desc': 'los ojos tristes,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'fermin',
    'cuando': '2020-01-24',
    'donde': 'asudsuas',
    'desc': 'los ojos tristes,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'jbm',
    'cuando': 'square up',
    'donde': 'jejejej',
    'desc': 'you acrting sussy,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'm',
    'cuando': '2020-01-24',
    'donde': 'fsdjkfsdjkdj',
    'desc': 'lil uzi vert,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'notepad',
    'cuando': '2020-01-24',
    'donde': 'share screen',
    'desc': 'willl smithh,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'vscode',
    'cuando': '2020-01-24',
    'donde': 'everyday ashbafskfj ',
    'desc': 'august,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'manolo',
    'cuando': '2020-01-24',
    'donde': 'manuel',
    'desc': 'heyyyy manuel',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'cetys men',
    'cuando': '2020-01-24',
    'donde': 'mock data ',
    'desc': 'willl smithh,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
  {
    'categoria': 'android studio',
    'cuando': '2020-01-24',
    'donde': 'omg ',
    'desc': 'jada,',
    'icon': 'https://bulma.io/images/placeholders/96x96.png',
  },
];

function Search() {
  const ITEMS_PER_PAGE = 4;
  const items = data;
  const numberOfPages = Math.ceil(items.length / ITEMS_PER_PAGE);

  const [currentPage, setCurrentPage] = useState(0);
  const [itemsShown, setItemsShown] = useState([]);

  useEffect(() => {
    const start = currentPage * ITEMS_PER_PAGE;
    const end = currentPage * ITEMS_PER_PAGE + ITEMS_PER_PAGE;
    const slice = items.slice(start, end);
    setItemsShown(slice);
  }, [currentPage]);

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
        <a className="pagination-link" onClick={() => {
          setCurrentPage(index);
        }}>{index + 1}</a>
      </li>
    );
  };

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
            {itemsShown.map((item, index) => (
              <Item key={index}
                icon={item.icon}
                categoria={item.categoria}
                donde={item.donde}
                cuando={item.cuando}
                desc={item.desc}/>
            ))}
          </div>
          <nav className="pagination">
            <a className="pagination-next logout">Log Out</a>
            <ul className="pagination-list">
              {[...Array(numberOfPages).keys()]
                  .map(updateCurrentItems)}
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}

export default Search;
