$(document).ready(function () {

$('#spanButton').hide();
var btMoedas = []

const widget = $("#dtpick").datepicker({
  language: 'pt-BR',
  todayHighlight: true,
  container: 'div.dtpic',
  format: 'dd/mm/yyyy'
}).hide();

widget.on('changeDate', function () {
  widget.hide();

  function monta_escolhas() {
    result = {}

    let tmp = $('.checkbox');

    console.log('Temp = ', tmp);
    const range = [0, 1, 2, 3]
    console.log('btMoedas = ', btMoedas);
    for (i in range) {
      if (btMoedas[i]) {
        result[`${tmp[i].id}`] = `${tmp[i].name}`
      }
    }
    console.log('Monta Escolhas = ', result);
    return result
  }

  const selectedDate = widget.datepicker('getFormattedDate');
  const moedas_escolhidas = monta_escolhas()
  const dd = JSON.stringify({ 'data': selectedDate, 'moedas': moedas_escolhidas })
  console.log('DADO ', dd);

  $.ajax({
    url: '/hoje',
    type: 'POST',
    data: dd,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    success: (result, status, request) => {
      $('.sec1, .sec2').hide();
      tmpdiv = { 'pp': '<div class="tab" id="tab1"></div>' };
      $('main').html(tmpdiv.pp);
      // console.log('Result = ', result);
      $('#tab1').html(result.response);
      console.log('Sucess', result.response);
    }
  })

});

$('#botao2').on('click', function () {

  btMoedas = [
    $('#Dolar').is(':checked'),
    $('#Euro').is(':checked'),
    $('#Libra').is(':checked'),
    $('#Shekel').is(':checked')
  ]

  $('#divMoedas').hide();
  $('#spanButton').show();
})

$('#botao').on('click', function () {
  const testo = $('#p2').text().trim()

  if (testo == 'p2') {
    $('#p1').text('clicou 1')
    $('#p2').text('Not p2')

    widget.show()

  } else {
    $('#p1').text('clicou 2')
    $('#p2').text('p2')

    widget.hide()

  }
});
});