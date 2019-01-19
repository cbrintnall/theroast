import GetUrl from './settings';
import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

// Components
import Header from "./components/header";

// Pages
import Index from './pages/index';
import Bean from './pages/beans';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header />
          <Route path={GetUrl("index")} exact component={Index}></Route>
          <Route path={GetUrl("beans")} exact component={Bean}></Route>
        </div>
      </Router>
    );
  }
}

export default App;
