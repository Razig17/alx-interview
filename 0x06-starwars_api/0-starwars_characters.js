#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response.statusCode === 200) {
      const characters = body.characters;
      const characterNames = [];
      characters.forEach((character, index) => {
        request(character, { json: true }, function (error, response, body) {
          if (error) {
            console.error('error:', error);
          } else {
            if (response.statusCode === 200) {
              characterNames[index] = body.name;
              if (characterNames.filter(name => name).length === characters.length) {
                characterNames.forEach(name => console.log(name));
              }
            }
          }
        });
      }
      );
    }
  }
}
);
