import React, { Component } from "react";

class Counter extends Component {
  state = {
    count: 0,
  };

  styles = {
    fontSize: 10,
    fontWeight: "bold",
  };

  handleIncreament = () => {
    this.state.count += 1;
    this.setState({cout: this.state.count + 1})
  }

  render() {
    return (
      <div>
        <span className={this.getBadgeClasses()} style={this.styles}>
          {this.formatCount()}
        </span>
        <button
          onClick={this.handleIncreament}
          className="btn btn-secondary btn-sm"
        >
          Increment
        </button>
      </div>
    );
  }

  getBadgeClasses() {
    let classes = "m-2 btn btn-";
    classes += this.state.count === 0 ? "warning" : "info";
    return classes;
  }

  formatCount() {
    const { count } = this.state;
    return count === 0 ? "Zero" : count;
  }
}

export default Counter;
