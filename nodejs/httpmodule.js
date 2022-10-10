const http = require('http');
const server = http.createServer((req, res) => {
    if (req.url === '/'){
        res.write('hello')
        res.end()
    }
    if (req.url === '/courses'){
        res.write(JSON.stringify([1,2,3]));
        res.end;
    }
});

server.on('connection', (socket) => {
    console.log('new connection');
})

server.listen('5000')

console.log('listening on 5000')

