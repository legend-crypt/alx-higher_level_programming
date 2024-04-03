#!/usr/bin/node

const header = $('header');
const clickHandler = $('DIV#update_header');

clickHandler.on('click', () => {
  header.text('New Header !!!');
});
