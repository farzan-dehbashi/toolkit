console.log('Before');
getUser(12, (usr) => {
    console.log(usr.id);
    console.log(usr.githuser);
});
console.log('after');

function getUser(id, callback) {
    setTimeout(() => {
        console.log('reading a user from a db');
        callback({id: id, githuser: 'farzan'})
    }, 2000)
}
