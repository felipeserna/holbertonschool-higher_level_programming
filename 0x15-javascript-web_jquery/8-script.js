/*
Write a Javascript script that fetches and lists all movies title by using
this URL: https://swapi-api.hbtn.io/api/films/?format=json

- All movie titles must be list in the HTML tag UL#list_movies
- You can’t use document.querySelector to select the HTML tag
- You must use the jQuery API
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('.result').html(data);
  let i = 0;
  while (i < data.count) {
    $('#list_movies').add('<li>' + data.results[i].title + '</li>').appendTo('#list_movies');
    i++;
  }
});
