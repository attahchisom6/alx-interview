#!/usr/bin/node


// this script prints character name from the api in the order in which they  fill the response list

const request = require('request');
async function getMovieNames(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}`;

  return new Promise((resolve, reject) => {
    if (error) {
      reject(error);
    }

    require(url, (error, response, body) => {
      const data = JSON.parse(body);
      const characters = data.characters;

      const promiseCharacterArray = await characters.map(charUrl => {
        return new Promise((charReject, charResolve) => {
          request(charUrl, (charError, charResponse, charBody) => {
            if (charError) {
              charResolve(charError);
            }
            charData = JSON.parse(body);
            charResolve(charData.name);
          });
        });
      });

      Promise.all(promiseCharacterArray)
      .then(characterNames => {
        resolve(characterNames);
      })
      .catch(error => {
        console.error(error);
      });
    });
  });
}

const movieId = process.argv[2]
if (!movieId) {
  console.log(`Usage: node ${process.argv[1]} <number>`);
} else {
  await getMovieNames(movieId)
    .then(characterNames => {
    characterNames.forEach(name => {
      console.log(name);
    });
  });
  .catch(error => {
    console.error(error);
  });
}
