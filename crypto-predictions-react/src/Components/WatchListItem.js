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
    this.setState(prevState => {
      return {
        active: !prevState.active
      }
    })
  }

  render () {
    let className = 'Databox-watchlist-item';
    if (this.state.active === true)
      className += ' Databox-active';
    
    return (
      <div className={className}>
        <p className="Databox-item-text">{this.props.text}</p>
      </div>
    )
  }
}

export default WatchListItem