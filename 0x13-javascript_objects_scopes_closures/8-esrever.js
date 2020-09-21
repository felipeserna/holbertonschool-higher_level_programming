#!/usr/bin/node
/*
Write a function that returns the reversed version of a list
*/
exports.esrever = function (list) {
  const list2 = [];
  let i = list.length - 1;
  while (i >= 0) {
    list2.push(list[i]);
    i--;
  }
  return list2;
};
