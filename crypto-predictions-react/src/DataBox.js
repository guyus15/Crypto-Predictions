import React from 'react';
import WatchListItem from './WatchListItem'
import NewsItem from './NewsItem'

class DataBox extends React.Component {
  constructor(props) {
    super(props);
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
            <div className={className}>
              <WatchListItem text="Test Text"></WatchListItem>
              <WatchListItem text="Test Text"></WatchListItem>
              <WatchListItem text="Test Text"></WatchListItem>
              <WatchListItem text="Test Text"></WatchListItem>
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