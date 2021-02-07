import React from 'react'
import Chart from 'chart.js'
import '../stylesheets/Graph-styles.css'

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidMount() {
    const myChartRef = this.chartRef.current.getContext("2d");

    let dataLabels = this.props.data.map(d => d.last_updated.substr(0,10));
    let dataValues = this.props.data.map(d => d.price);

    this.myChart = new Chart(myChartRef, {
      type: 'line',
      color:'rgba(0,0,0,1)',
      options: {
        responsive: true,
        maintainAspectRatio: false
      },
      data: {
        labels:dataLabels,
        datasets: [{
          label: this.props.title,
          data: dataValues,
          backgroundColor: this.props.color,
          borderColor: this.props.borderColor,
          borderWidth: this.props.borderWidth,
          lineTension: 0
        }]
      }
    });
  }

  render() {
    return (
      <div className="Graph-container">
        <canvas
          id="myChart" 
          ref={this.chartRef}
        />
      </div>
    )
  }
}

export default Graph