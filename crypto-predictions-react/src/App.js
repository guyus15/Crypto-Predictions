import React from 'react';
import logo from './logo.svg';
import './App.css';
import DataBox from './Components/DataBox';
import CurrentPrice from './Components/CurrentPrice'
import Graph from './Components/Graph'

let timeSeries = {
  "title": "Visits",
  "data": [
    {
      "time": "Tue May 01 2018 00:00:00 GMT+0100 (British Summer Time)",
      "value": 39
    },
    {
      "time": "Wed May 02 2018 00:00:00 GMT+0100 (British Summer Time)",
      "value": 60
    },
    {
      "time": "Wed June 02 2018 00:00:00 GMT+0100 (British Summer Time)",
      "value": 60
    },
    {
      "time": "Wed August 02 2018 00:00:00 GMT+0100 (British Summer Time)",
      "value": 60
    }
  ]
}

let categoricalData = {
  "title": "Categories",
  "data": [
    {
      "label": "A",
      "value": 46
    },
    {
      "label": "B",
      "value": 87
    },
    {
      "label": "C",
      "value": 112
    },
    {
      "label": "D",
      "value": 190
    },
  ]
}


class App extends React.Component {
  render() {
    return (
      <div className="App-container">
          <CurrentPrice name="Bitcoin (BTC)" price="27500"></CurrentPrice>
          <Graph
            data={categoricalData}
            title="Test graph title"
            color="#70CAD1"
          />
          <div className="Databoxes">
            <DataBox title="Watchlist" type="watchlist"></DataBox>
            <DataBox title="Trending Stories" type="news"></DataBox>
          </div>
      </div>
    )
  }
}

export default App;

