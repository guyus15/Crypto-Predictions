import React from 'react';
import logo from './logo.svg';
import './App.css';
import DataBox from './Components/DataBox';
import CurrentPrice from './Components/CurrentPrice'
import Graph from './Components/Graph'

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
  constructor() {
    super();

    this.state = {
      currencyInfo: this.getInfo()
    } 

    this.getInfo = this.getInfo.bind(this);
    //this.getPrice = this.getPrice.bind(this);
  }

  
  getInfo() {
    let currency = 'Bitcoin';
    fetch(`/getinfo?currency=${currency}`)
      .then(res => res.json())
      .then(data => {
        this.setState({currencyInfo: data})
      });
  }

  render() {
    console.log(this.state.currencyInfo);

    let currencyName = "Test currency"
    let currencyPrice = "27500" 
    
    if (this.state.currencyInfo !== undefined) {
      currencyName = `${this.state.currencyInfo.name} (${this.state.currencyInfo.symbol}) `;
    }

    return (
      <div className="App-container">
          <CurrentPrice name={currencyName} price={currencyPrice}></CurrentPrice>
          <Graph
            data={categoricalData}
            title={currencyName}
            color="rgba(0,0,0,0)"
            borderColor="#FFF"
            borderWidth={3}
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

