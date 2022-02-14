import React from 'react';
import ReactDom from 'react-dom';

const element = <h1>Hello world</h1> ;
// saves changes
// console.log(element) 

//render the object to show it
ReactDom.render(element, document.getElementById('root'));