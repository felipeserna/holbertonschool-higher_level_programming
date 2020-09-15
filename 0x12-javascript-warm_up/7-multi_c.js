#!/usr/bin/node
/*
Prints x times
C is fun
*/
if (!process.argv[2]) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('C is fun');
}
