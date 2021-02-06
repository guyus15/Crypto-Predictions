import React from 'react';
import logo from './logo.svg';
import './App.css';
import DataBox from './DataBox';


class App extends React.Component {
  render() {
    return (
      <div className="App-container">
          <div className="Databoxes">
            <DataBox title="Watchlist" type="watchlist"></DataBox>
            <DataBox title="Trending Stories" type="news"></DataBox>
          </div>
      </div>
    )
  }
}

export default App;

