import React, { useEffect } from 'react';
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
      currencyInfo: undefined,
      currencyPrice: [{"last_updated":"","price":"","percentage_change_1h":"","percent_change_24h":"", "percentage_change_7d":""}],
      currencyNews: [{"content":"","image_url":"","last_updated":"","published_at":"","title":"","url":"","uuid":""}],
      time: Date.now()
    } 

    this.getInfo = this.getInfo.bind(this);
    this.getPrice = this.getPrice.bind(this);
    this.getGraph = this.getGraph.bind(this);
    this.updateCurrency = this.updateCurrency.bind(this);
  }

  
  getInfo(currency) {
    fetch(`/getinfo?currency=${currency}`)
      .then(res => res.json())
      .then(data => {
        this.setState({currencyInfo: data})
      });
  }

  getPrice(currency) {
    fetch(`/getprice?currency=${currency}`)
      .then(res => res.json())
      .then(data => {
        this.setState({currencyPrice: data})
      });
  }

  getNews(currency) {
    fetch(`/getnews?currency=${currency}`)
      .then(res => res.json())
      .then(data => {
        this.setState({currencyNews: data})
      });
  }

  updateCurrency() {
    if (localStorage.getItem('currency') === null)
    {
      localStorage.setItem('currency', 'bitcoin');
    }

    let currentCurrency = localStorage.getItem('currency'); 

    this.getInfo(currentCurrency);
    this.getPrice(currentCurrency);
    this.getNews(currentCurrency);
  }

  componentDidMount() {
    this.updateCurrency();
  }

  getGraph(priceData, currencyName) {
    return (
      <Graph
        data={priceData}
        title={currencyName}
        color="rgba(0,0,0,0)"
        borderColor="#FFF"
        borderWidth={3}
      />            
    )
  }

  render() {
    
    let priceData = this.state.currencyPrice;
    let currencyName = "Currency"
    let currencyPrice = "27500"
    let currencyDesc = ""
    let currencyDateCreated = ""
    let currentNewsData = ""
    
    if (this.state.currencyInfo !== undefined && this.state.currencyPrice !== undefined) {
      currencyName = `${this.state.currencyInfo.name} (${this.state.currencyInfo.symbol})`;
      currencyPrice = priceData[priceData.length - 1].price;
      currencyDesc = this.state.currencyInfo.description;
      currencyDateCreated = this.state.currencyInfo.date_added;
    }

    if (this.state.currencyNews !== undefined) {
      currentNewsData = this.state.currencyNews;
    }

    return (
      <div className="App-container">
          <CurrentPrice name={currencyName} price={currencyPrice}></CurrentPrice>
          {this.getGraph(priceData,currencyName)}
          <div className="Databoxes">
            <DataBox 
              title="Watchlist"
              type="watchlist"
              updateCurrency={this.updateCurrency}
            ></DataBox>
            <DataBox title="Information"
              type="information"
              updateCurrency={this.updateCurrency}
              description={currencyDesc}
              dateAdded={"Date Added: " + currencyDateCreated}
            ></DataBox>
            <DataBox
              title="Trending Stories"
              type="news"
              updateCurrency={this.updateCurrency}
              newsData={currentNewsData}
            ></DataBox>
          </div>
      </div>
    )
  }
}

export default App;

