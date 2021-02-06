import React from 'react'
import '../stylesheets/CurrentPrice-styles.css'

class CurrentPrice extends React.Component {
  render() {
    return (
      <div className="CurrentPrice-container">
        <p className="CurrentPrice-name">{this.props.name}</p>
        <p className="CurrentPrice-price">£{this.props.price}</p>
        <p className="CurrentPrice-text">Current Price</p>
      </div>
    )
  }
}

export default CurrentPrice