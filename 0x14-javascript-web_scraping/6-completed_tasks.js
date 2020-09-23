#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id.

- The first argument is the
  API URL: https://jsonplaceholder.typicode.com/todos
- You must use the module request
*/
const request = require('request');

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = {};
    for (const data of body) {
      if (data.completed) {
        if (result[data.userId]) {
          result[data.userId] += 1;
        } else {
          result[data.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
