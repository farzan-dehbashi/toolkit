const p1 = new Promise((resolve, reject) => {
    // lets access a db and some async stuff
    setTimeout(() => {    const job= 'workedd'
    if (job === "worked") resolve("p1 worked");
    else  reject(new Error('message is error'))
    }, 2000);
});

const p2 = new Promise((resolve, reject) => {
    // lets access a db and some async stuff
    setTimeout(() => {    const job= 'worked'
    if (job === "worked") resolve("p2 worked");
    else  reject(new Error('message is error'))
    }, 1000);
});

Promise.all([p1,p2])
    .then(result => {console.log(result)})
    .catch(err => console.log('Error', err.message))
