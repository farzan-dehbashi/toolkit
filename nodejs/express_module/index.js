const express = require('express');
const app = express()

const courses = [
    {id: 1, name: 'course1'},
    {id: 2, name: 'course2'},
    {id: 3, name: 'course3'},
];

app.get('/', (req,res) => {
    res.send('hello world')
});

app.get('/api/courses', (req, res) => {
    res.send(courses)
})

app.get('/api/courses/:id', (req, res) => {
    const course = courses.find(c => c.id === parseInt(req.params.id))
    if (!course) // 404
    {
        res.status(404).send('The course with the given id not found')
    }
    else res.send(course)
});

app.post('/api/courses', (req, res) =>{
    if (!req.body.name || req.body.name.length < 3) {
        res.status(400)
    }
});

const PORT  = process.env.PORT || 4000
app.listen(PORT, () => {console.log(`started to listen on port ${PORT}`)})
