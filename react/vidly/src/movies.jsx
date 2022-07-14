import React, { Component } from 'react';
import {getMovies} from './services/fakeMovieService';

class Movies extends Component {
    state = {  
        movies: [
            {
              _id: "5b21ca3eeb7f6fbccd471815",
              title: "Terminator",
              genre: { _id: "5b21ca3eeb7f6fbccd471818", name: "Action" },
              numberInStock: 6,
              dailyRentalRate: 2.5,
              publishDate: "2018-01-03T19:04:28.809Z"
            },
            {
              _id: "5b21ca3eeb7f6fbccd471816",
              title: "Die Hard",
              genre: { _id: "5b21ca3eeb7f6fbccd471818", name: "Action" },
              numberInStock: 5,
              dailyRentalRate: 2.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd471817",
              title: "Get Out",
              genre: { _id: "5b21ca3eeb7f6fbccd471820", name: "Thriller" },
              numberInStock: 8,
              dailyRentalRate: 3.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd471819",
              title: "Trip to Italy",
              genre: { _id: "5b21ca3eeb7f6fbccd471814", name: "Comedy" },
              numberInStock: 7,
              dailyRentalRate: 3.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd47181a",
              title: "Airplane",
              genre: { _id: "5b21ca3eeb7f6fbccd471814", name: "Comedy" },
              numberInStock: 7,
              dailyRentalRate: 3.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd47181b",
              title: "Wedding Crashers",
              genre: { _id: "5b21ca3eeb7f6fbccd471814", name: "Comedy" },
              numberInStock: 7,
              dailyRentalRate: 3.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd47181e",
              title: "Gone Girl",
              genre: { _id: "5b21ca3eeb7f6fbccd471820", name: "Thriller" },
              numberInStock: 7,
              dailyRentalRate: 4.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd47181f",
              title: "The Sixth Sense",
              genre: { _id: "5b21ca3eeb7f6fbccd471820", name: "Thriller" },
              numberInStock: 4,
              dailyRentalRate: 3.5
            },
            {
              _id: "5b21ca3eeb7f6fbccd471821",
              title: "The Avengers",
              genre: { _id: "5b21ca3eeb7f6fbccd471818", name: "Action" },
              numberInStock: 7,
              dailyRentalRate: 3.5
            }
          ]
    };
    
    
    render() { 
        return <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Genre</th>
                    <th>Stock</th>
                    <th>Rate</th>
                </tr>
            </thead>
            <tbody>
                {this.state.movies.map(movie => 
                <tr>
                    <td>{movie.title}</td>
                    <td>{movie.genre.name}</td>
                    <td>{movie.numberInStock}</td>
                    <td>{movie.dailyRentalRate}</td>
                </tr>
                )}
            </tbody>
        </table>
    }
}
 
export default Movies;