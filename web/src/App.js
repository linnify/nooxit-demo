import React from 'react';
import './App.css';
import logo from './assets/logo.png';
import {  BrowserRouter as Router } from "react-router-dom";
import Home from "./pages/Home";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
  
      <Router>
        <Home />
      </Router>
    </div>
  );
}

export default App;
