/*
Write a Javascript script that fetches from
https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello
from that fetch in the HTML’s tag DIV#hello.

- The translation of “hello” must be display in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the HEAD tag
*/
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').append(`${data.hello}`);
});
