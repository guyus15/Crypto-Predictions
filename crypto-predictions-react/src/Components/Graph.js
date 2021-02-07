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

    let dataLabels = this.props.data.data.map(d => d.label);
    let dataValues = this.props.data.data.map(d => d.value);

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