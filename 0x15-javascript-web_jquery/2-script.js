/*
Write a Javascript script that updates the text color of
the HTML tag HEADER to red (#FF0000) when the user clicks on
the tag DIV#red_header:

- You can’t use document.querySelector to select the HTML tag
- You must use the jQuery API
*/
$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
