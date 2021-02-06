import React from 'react'

class NewsItem extends React.Component {
  render () {
    return (
      <div className='Databox-list-item'>
        <p className="Databox-item-text">{this.props.text}</p>
        <p className="Databox-item-subtext">{this.props.date}</p>
      </div>
    )
  }
}

export default NewsItem