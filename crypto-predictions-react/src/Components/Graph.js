import React from 'react'
import Chart from 'chart.js'

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidMount() {
    let dataLabels = this.props.data.data.map(d => d.label);
    let dataValues = this.props.data.data.map(d => d.value);

    this.myChart = new Chart(this.chartRef.current, {
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
          backgroundColor: this.props.color
        }]
      }
    });

    this.chartRef.current.style = "width: 1870px; height: 340px";
  }

  render() {
    return (
      <canvas className="Graph-canvas" ref={this.chartRef} />
    )
  }
}

export default Graph