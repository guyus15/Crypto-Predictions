import React from 'react';
import WatchListItem from './WatchListItem'
import NewsItem from './NewsItem'
import '../stylesheets/DataBox-styles.css'

class DataBox extends React.Component {
  constructor(props) {
    super(props);

    this.updateDatabox = this.updateDatabox.bind(this);
  }

  updateDatabox () {
    this.props.updateCurrency();
  }

  render() {
    let className = "Databox";
    if (this.props.type === "watchlist")
      className += " Databox-watchlist";
    else 
      className += " Databox-list"

    return (
      <div className='Databox-container'>
        <p className='Databox-title'>{this.props.title}</p>
        
          {this.props.type === "watchlist" ? (
            <div className={className} onClick={this.updateDatabox}>
              <WatchListItem text="Bitcoin (BTC)" currency="bitcoin" updateDatabox={this.updateDatabox}></WatchListItem>
              <WatchListItem text="Ethereum (ETH)" currency="ethereum" updateDatabox={this.updateDatabox}></WatchListItem>
              <WatchListItem text="Litecoin (LTC)" currency="litecoin" updateDatabox={this.updateDatabox}></WatchListItem>
              <WatchListItem text="Dogecoin (DOGE)" currency="dogecoin" updateDatabox={this.updateDatabox}></WatchListItem>
              <WatchListItem text="Binance Coin (BNB)" currency="binance" updateDatabox={this.updateDatabox}></WatchListItem>
              <WatchListItem text="Bitcoin Cash (BCH)" currency="bitcoin_cash" updateDatabox={this.updateDatabox}></WatchListItem>
            </div>
            ) : this.props.type === "information" ? (
            <div className={className}>
              <p>This is an information box</p>
            </div>
            ) : (
            <div className={className}>
              <NewsItem text="Text text" date="02/02/2021"></NewsItem>
              <NewsItem text="Text text" date="02/02/2021"></NewsItem>
              <NewsItem text="Text text" date="02/02/2021"></NewsItem>
              <NewsItem text="Text text" date="02/02/2021"></NewsItem>
            </div>
            )}
      </div>
    )
  }
}


export default DataBox;