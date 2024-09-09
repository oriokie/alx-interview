#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        else if (response.statusCode !== 200) reject(new Error(`Invalid status code: ${response.statusCode}`));
        else resolve(JSON.parse(body).name);
      });
    });
  };

  Promise.all(characterUrls.map(fetchCharacter))
    .then(names => names.forEach(name => console.log(name)))
    .catch(error => console.error('Error:', error));
});
