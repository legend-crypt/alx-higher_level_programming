#!/usr/bin/node

$(document).ready(() => {;
const field = $('DIV#hello');

  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    field.text(data.hello);
  });
});
