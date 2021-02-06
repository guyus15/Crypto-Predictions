import React from 'react'
import Chart from 'chart.js'
import '../stylesheets/Graph-styles.css'

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidMount() {

    console.log(this.props.data.data);
    let dataLabels = this.props.data.data.map(d => d.label);
    let dataValues = this.props.data.data.map(d => d.value);

    this.myChart = new Chart(this.chartRef.current, {
      type: 'line',
      data: {
        labels:dataLabels,
        datasets: [{
          label: this.props.title,
          data: dataValues,
          backgroundColor: this.props.color
        }]
      }
    });
  }

  render() {
    return (
      <canvas className="Graph-canvas" ref={this.chartRef} />
    )
  }
}

export default Graph