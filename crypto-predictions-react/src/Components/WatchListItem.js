import React from 'react'

class WatchListItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      active: false
    }
    this.toggleActive = this.toggleActive.bind(this);
  }
  
  toggleActive() {
    const currentCurrency = document.querySelector('.CurrentPrice-name');
    if(this.props.text !== currentCurrency.text){
      this.setState(prevState => {
        return {
          active: !prevState.active
        }
      });
      localStorage.setItem("currency", this.props.currency);
    }
  }

  render () {
    let className = 'Databox-watchlist-item';
    if (this.state.active === true)
      className += ' Databox-active';
    
    return (
      <div className={className} onClick={this.toggleActive}>
        <p className="Databox-watchlist-text">{this.props.text}</p>
      </div>
    )
  }
}

export default WatchListItem