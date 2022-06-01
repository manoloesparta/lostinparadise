// Libraries
import React from "react";
import {
  Routes,
  Route,
  Navigate,
  BrowserRouter as Router,
} from "react-router-dom";

// Components
import Search from "./pages/Search";
import Login from "./pages/Login";
import Private from "./pages/Private";
import { AuthProvider } from "./utils/auth";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="*" element={<NotFound />} />
          <Route path="/search" element={<Private />}>
            <Route path="/search" element={<Search />} />
          </Route>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </div>
  );
}

export default () => {
  return (
    <AuthProvider>
      <App />
    </AuthProvider>
  );
};
