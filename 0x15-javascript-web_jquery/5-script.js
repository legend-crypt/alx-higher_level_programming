#!/usr/bin/node

const ul = $('UL.my_list');
const handleClick = $('DIV#add_item');

handleClick.on('click', () => {
  ul.append('<li>Item</li>');
});
