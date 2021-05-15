// this is the best comment ever X 10
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (info) {
  $('#character').append(info.name);
});
