import React from 'react'
import Chart from 'chart.js'

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidMount() {
    this.myChart = new Chart(this.canvasRef.current, {
      type: 'bar'
    });
  }

  render() {
    return (
      <canvas />
    )
  }
}

export default Graph