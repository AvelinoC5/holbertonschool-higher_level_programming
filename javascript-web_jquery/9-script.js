$(function () {

    $.ajax({
      type: 'GET',
      url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
      success: function (input) {
        $("DIV#hello").text(input.hello);
      }
    });
  });