/*
Write a Javascript script that fetches and replaces the name of this
URL: https://swapi-api.hbtn.io/api/people/5/?format=json

- The name must be displayed in the HTML tag DIV#character
- You can’t use document.querySelector to select the HTML tag
- You must use the jQuery API
*/
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, data => $('DIV#character').text(data.name));
