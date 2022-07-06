import React, { Component } from "react";

class Counter extends Component {
    state = {
        count: 1,

    };

    styles = {
        fontSize: 10,
        fontWeight: "bold"
    };

  render() {

    return (
      <div>
        <span className={this.getBadgeClasses()} style={this.styles}>
            {this.formatCount()}
        </span>
        <button className="btn btn-secondary btn-sm">Increment</button>
      </div>
    );
  }

    getBadgeClasses() {
        let classes = "m-2 btn btn-";
        classes += this.state.count === 0 ? "warning" : "info";
    }

  formatCount(){
    const {count} = this.state;
    return count === 0 ? 'Zero' : count;
  }
}

export default Counter;
