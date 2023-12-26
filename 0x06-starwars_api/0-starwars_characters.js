#!/usr/bin/node

const request = require('request-promise');

function getCharacterEndPoints(filmID) {
  const filmURL = `https://swapi-api.alx-tools.com/api/films/${filmID}`;
  return request(filmURL).then(body => JSON.parse(body).characters);
}

async function getCharacterNames(starWarID) {
  try {
    const characterEndPoints = await getCharacterEndPoints(starWarID);
    const requests = characterEndPoints.map(element => request(element).then(body => JSON.parse(body).name));
    const characterNames = await Promise.all(requests);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.log(error);
  }
}

const starWarID = process.argv[2];
getCharacterNames(starWarID);

