import React from 'react';
import WatchListItem from './WatchListItem'
import NewsItem from './NewsItem'
import '../stylesheets/DataBox-styles.css'

class DataBox extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      toggle: false
    }

    this.updateDatabox = this.updateDatabox.bind(this);
    this.resetWatchlistActive = this.resetWatchlistActive.bind(this);
  }

  resetWatchlistActive() 
  {
    this.setState(prevState => {
      return {
        toggle: !prevState.toggle
      }
    })
  }

  updateDatabox () {
    this.props.updateCurrency();
  }

  render() {
    let className = "Databox";
    if (this.props.type === "watchlist")
      className += " Databox-watchlist";
    else if (this.props.type === "information")
      className += " Databox-information"
    else 
      className += " Databox-list"

    return (
      <div className='Databox-container'>
        <p className='Databox-title'>{this.props.title}</p>
        
          {this.props.type === "watchlist" ? (
            <div className={className} onClick={this.updateDatabox}>
              <WatchListItem text="Bitcoin (BTC)" currency="bitcoin" updateDatabox={this.updateDatabox} reset={this.resetWatchlistActive}></WatchListItem>
              <WatchListItem text="Ethereum (ETH)" currency="ethereum" updateDatabox={this.updateDatabox} reset={this.resetWatchlistActive}></WatchListItem>
              <WatchListItem text="Litecoin (LTC)" currency="litecoin" updateDatabox={this.updateDatabox} reset={this.resetWatchlistActive}></WatchListItem>
              <WatchListItem text="Dogecoin (DOGE)" currency="dogecoin" updateDatabox={this.updateDatabox} reset={this.resetWatchlistActive}></WatchListItem>
              <WatchListItem text="Binance Coin (BNB)" currency="binance" updateDatabox={this.updateDatabox} reset={this.resetWatchlistActive}></WatchListItem>
              <WatchListItem text="Bitcoin Cash (BCH)" currency="bitcoin_cash" updateDatabox={this.updateDatabox} reset={this.resetWatchlistActive}></WatchListItem>
            </div>
            ) : this.props.type === "information" ? (
            <div className={className}>
              <p className="Databox-info-desc">{this.props.description}</p>
              <p className="Databox-info-date">{this.props.dateAdded.substr(0, 22)}</p>
            </div>
            ) : (
            <div className={className}>
              {this.props.newsData.map(article => <NewsItem text={article.title} date={article.published_at.substr(0,10)}></NewsItem>)}

            </div>
            )}
      </div>
    )
  }
}


export default DataBox;