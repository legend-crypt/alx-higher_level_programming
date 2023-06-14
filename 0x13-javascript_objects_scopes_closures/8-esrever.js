#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length - 1;
  const newArr = [];
  for (i; i >= 0; i--) {
    newArr.push(list[i]);
  }
  return newArr;
};
