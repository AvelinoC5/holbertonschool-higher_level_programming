$(function () {
    var $pelis = $("UL#list_movies");
  
    $.ajax({
      type: 'GET',
      url: 'https://swapi-api.hbtn.io/api/films/?format=json',
      success: function (movies) {
        $.each(movies.results, function (i, movie) {
          $pelis.append('<li>' + movie.title + '</li>');
        });
      }
    });
  });