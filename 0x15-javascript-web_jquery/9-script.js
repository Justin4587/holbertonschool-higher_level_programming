// this is the best comment ever X 10
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (info) {
  $('#hello').append(info.hello);
});
