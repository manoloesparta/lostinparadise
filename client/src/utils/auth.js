import React, {useState, createContext, useContext, useEffect} from 'react';

const API_URL = 'http://localhost:5000';
const authContext = createContext();

function useProvideAuth() {
  const [authed, setAuthed] = useState(false);

  const token = localStorage.getItem('user_token');
  const config = {'method': 'POST', 'headers': {'x-jwt-key': token}};

  useEffect(async () => {
    if (token) {
      const response = await fetch(API_URL + '/validate', config);
      if (response.status == 200) {
        setAuthed(true);
      } else {
        localStorage.removeItem('user_token');
      }
    }
  }, []);

  const login = async (username, password) => {
    const config = {
      'method': 'POST',
      'body': JSON.stringify({username, password}),
    };

    const response = await fetch(API_URL + '/login', config);

    if (response.status == 201) {
      const json = await response.json();
      const token = json.data['x-jwt-key'];
      localStorage.setItem('user_token', token);
      setAuthed(true);
      return token;
    }
  };

  const logout = () => {
    localStorage.removeItem('user_token');
    setAuthed(false);
  };

  return {
    authed,
    login,
    logout,
  };
}

export function AuthProvider({children}) {
  const auth = useProvideAuth();

  return (
    <authContext.Provider value={auth}>
      {children}
    </authContext.Provider>
  );
}

export default function useAuth() {
  return useContext(authContext);
}
