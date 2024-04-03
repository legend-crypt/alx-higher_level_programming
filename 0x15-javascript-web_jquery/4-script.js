const header = $('header');
const clickHandler = $('DIV#toggle_header');

clickHandler.on('click', () => {
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
})