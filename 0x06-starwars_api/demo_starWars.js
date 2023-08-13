#!/usr/bin/node

// script fetch names of actors from a film starwars api in rhe order in which they fill in the response list

const request = require('request');

async function getMovieNames(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}`;

  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      const data = JSON.parse(body);
      const characters = data.characters;

      const promiseCharacterArray = characters.map(charUrl => {
        return new Promise((charResolve, charReject) => {
          request(charUrl, (charError, charResponse, charBody) => {
            if (charError) {
              charReject(charError);
              return;
            }
            charData = JSON.parse(charBody);
            charResolve(charData.name);
          });
        });
      });

      Promise.all(promiseCharacterArray)
      .then(characterNames => {
        resolve(characterNames);
      })
      .catch(error => {
        reject(error);
      });
    });
  });
}

const movieId = process.argv[2]
if (!movieId) {
  console.log(`Usage: node ${process.argv[1]} <number>`);
} else {
  getMovieNames(movieId)
  .then(characterNames => {
    characterNames.forEach(name => {
      console.log(name);
    });
  })
  .catch(error => {
    console.error(error);
  });
}
