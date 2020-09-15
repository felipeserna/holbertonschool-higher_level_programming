#!/usr/bin/node
/*
Prints a square
The first argument is the size of the square
*/
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
}
for (let i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('X'.repeat(process.argv[2]));
}
