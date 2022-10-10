class Logger extends EventEmitter {
    log(message) {
      console.log(message)

      this.emit('event_to_raise', {id: 123, message:"hi"})
    }
}

module.exports = Logger;
