const fs = require('fs');

const files = fs.readdirSync('./');

console.log(files)

fs.readdir('$', function(err, files){
    if (err) console.log("error ", err);
    else console.log('Result async: ', files)
});

