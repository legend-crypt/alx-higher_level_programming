#!/usr/bin/node
const request = require('request');

if (!process.argv || process.argv.length < 3) {
  process.exit(1);
}
const taskObj = {};
const taskCompleted = () => {
  const url = process.argv[2] + '?completed=true';
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }
    const datas = JSON.parse(body);
    datas.forEach((data) => {
      if (taskObj[data.userId]) {
        taskObj[data.userId] += 1;
      } else {
        taskObj[data.userId] = 1;
      }
    });
    console.log(taskObj);
  });
};
taskCompleted();
