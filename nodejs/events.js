const EventEmitter = require('events');
const emitter = new EventEmitter();

emitter.on('event_to_raise', (e) => {
console.log('event raised', e);
});

emitter.emit('event_to_raise', {id: 1, url: 'http://'})
