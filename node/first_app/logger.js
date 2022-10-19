
    console.log(__filename)
    console.log(__dirname)
    var url = 'http://github.com/';

    function log(message) {
        // send http request
        console.log(message);
    }

    module.exports.log = log;
    module.exports.url = url;
