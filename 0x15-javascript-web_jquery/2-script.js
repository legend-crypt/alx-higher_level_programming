#!/usr/bin/node
const header = $('header');
const onClickHandler = $('DIV#red_header');

onClickHandler.on('click', () => {
  header.css('color', '#FF0000');
});
