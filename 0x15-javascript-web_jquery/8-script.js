// this is the best comment ever X 10
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (info) {
  $.each(info.results, function (index, value) {
    $('#list_movies').append(value.title);
  });
});
