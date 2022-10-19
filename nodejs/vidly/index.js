const express = require('express')
const router = express.Router();

app.use(express.json());

const movies = [
    {id:1, name:"movie1"},
    {id:2, name:"movie2"},
    {id:3, name:"movie3"}
];

router.get('/', (req,res) => {
    res.send('Welcome to vidly')
});

router.get('/api/list', (req, res) => {
    res.send(movies)
})

router.get('/api/:id', (req, res)=>{
    const movie = movies.find(movie => movie.id === req.params.id)
    if (!movie) res.status(404).send('Movie not found')
    else res.send(movie)
})

router.post('/api/movies', (req, res) => {
    const movie = {
        id: movies.length + 1,
        name: req.body.name
    }
    movies.push(movie);
    res.send(movie);
})
