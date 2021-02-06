import React from 'react';
import logo from './logo.svg';
import './App.css';
import DataBox from './Components/DataBox';
import CurrentPrice from './Components/CurrentPrice'

class App extends React.Component {
  render() {
    return (
      <div className="App-container">
          <CurrentPrice name="Bitcoin (BTC)" price="27500"></CurrentPrice>
          <div style={{height: '38%'}}></div> {/*Placeholder div to represent the graph*/}
          <div className="Databoxes">
            <DataBox title="Watchlist" type="watchlist"></DataBox>
            <DataBox title="Trending Stories" type="news"></DataBox>
          </div>
      </div>
    )
  }
}

export default App;

