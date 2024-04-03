#!/usr/bin/node
const header = $('header');
const onClickHandler = $('DIV#red_header');

onClickHandler.on('click', () => {
  header.addClass('red');
});
