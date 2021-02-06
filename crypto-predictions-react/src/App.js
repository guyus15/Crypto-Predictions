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

    /*
    this.state = {
      currencyPrice: this.getPrice(),
      currencyInfo: this.getInfo() 
    }

    //this.getInfo = this.getInfo.bind(this);
    //this.getPrice = this.getPrice.bind(this);*/
  }

  /*
  getInfo() {
    let currency = 'ethereum';
    fetch(`/getinfo?currency=${currency}`)
      .then(res => res.json())
      .then(data => {
        this.setState({currencyInfo: data})
      });
  }

  getPrice() {
    let currency = 'ethereum';
    fetch(`/getprice?currency=${currency}`)
      .then(res => res.json())
      .then(data => { 
        this.setState({currencyPrice: data})
      });
  }*/

  render() {
    
    let currencyName = "Test currency"
    let currencyPrice = "27500" 
    /*
    if (this.state.currencyPrice !== undefined) {
      currencyName = `${this.state.currencyPrice[0].name} (${this.state.currencyPrice[0].symbol}) `;
      currencyPrice = this.state.currencyPrice[0].quote.GBP.price;
      console.log(this.state.currencyPrice);
    }*/


    return (
      <div className="App-container">
          <CurrentPrice name={currencyName} price={currencyPrice}></CurrentPrice>
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

