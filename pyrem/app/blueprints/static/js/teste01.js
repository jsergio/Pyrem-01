$(document).ready(function () {
  // Dados que serão enviados para o servidor
  var data_to_send = {
    key1: 'value1',
    key2: 'value2'
  };

  // Fazendo a requisição AJAX
  $.ajax({
    type: 'POST',
    url: '/data',
    contentType: 'application/json',
    data: JSON.stringify(data_to_send),
    success: function (response) {
      $('#result').text(response.processed_data);
      console.log('OK ', response);
    },
    error: function (xhr, status, error) {
      console.error(error);
    }
  });
});