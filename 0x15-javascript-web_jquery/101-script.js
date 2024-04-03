#!/usr/bin/node
$(document).ready(() => {
    const ul = $('UL.my_list');
    const handleAddItem = $('DIV#add_item');
    const handleRemoveItem = $('DIV#remove_item');
    const handleClearList = $('DIV#clear_list');

    handleAddItem.on('click', () => {
        ul.append('<li>Item</li>');
        }
    );
    handleRemoveItem.on('click', () => {
        ul.children().last().remove();
        }
    );
    handleClearList.on('click', () => {
        ul.empty();
        }
    );
});
