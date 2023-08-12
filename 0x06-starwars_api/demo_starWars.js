#!/usr/bin/node

// this script printcharacter name from the api in the order in which they  fill the response list
const request = require("request");
async function getMovieNames(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}`;

  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }

      const data = JSON.parse(body);
      const characters = data.characters;

      const promiseCharacterArray = characters.map(charUrl => {
        return new Promise((charResolve, charReject) => {
          request(charUrl, (charError, charResponse, charBody) => {
            if (charError) {
              charReject(charError);
            }
            const charData = JSON.parse(charBody)
            resolve(charData.name)
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
};

const movieId = process.argv[2]
if (!movieId) {
  console.log(`Usage: node ${process.argv[1]} <number>`);
} else {
  getMovieNames(movieId)
  .then(characterNames => {
    characterNames.forEach(name => {
      console.log(name);
    })
  })
  .catch(error => {
    console.error(error);
  });
}
