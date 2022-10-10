const p = new Promise((resolve, reject) => {
    // lets access a db and some async stuff
    setTimeout(() => {    const job= 'workedd'
    if (job === "worked") resolve(1);
    else  reject(new Error('message is error'))
    }, 2000);
});

p
    .then(result => {console.log(result)})
    .catch(err => console.log('Error', err.message))
