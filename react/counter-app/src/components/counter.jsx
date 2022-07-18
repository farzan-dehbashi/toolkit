import React, { Component } from 'react';

class Counter extends Component {

    state = {
        count : 0
    };

    handleIncreament= () => {
        this.setState({count: this.state.count + 1})
    }

    render() { 
        let classes = "badge m-2 badge-";
        classes += (this.state.count ==0) ? "warning" : "primary";

        return (
            <div>
                <span className={classes}>{this.formatCount(this.state.count)}</span>
                <button onClick={this.handleIncreament} className='btn btn-secondary btn-sm'>Increase</button>
            </div>
        );
    }

    formatCount(){
        const {count} = this.state;
        return count === 0 ? "Zero" : count;
    }
}
 
export default Counter;