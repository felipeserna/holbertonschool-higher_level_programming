#!/usr/bin/node
/*
Write a script that prints the number of movies where the
character “Wedge Antilles” is present.

- The first argument is the API URL of the Star wars
  API: https://swapi-api.hbtn.io/api/films/
- Wedge Antilles is character ID 18
- You must use the module request

i = film
j = character
*/
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
