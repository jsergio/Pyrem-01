/*  $(document).ready(function () {

    const widget = $('#dtpick').datepicker({

      language: 'pt-BR',
      todayHighlight: true,
      container: 'div.dtpic',
      format: "dd/mm/yyyy"
    }).hide();


    widget.on('changeDate', function () {
      const selectedDate = widget.datepicker('getFormattedDate');
      let dd = JSON.stringify({ 'data': selectedDate })
      // $('#resp').html(selectdate)
      // $.post('/b', { 'data': selectdate }, (data) => $('scan').html(data)
      // , 400)
      $.ajax({
        url: '/b',
        type: 'POST',
        //data: JSON.stringify(usuario),
        //data: {'id': '7', 'nome': 'BRUNO'},
        data: dd,
        //data: usuario,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function (result, status, request) {
          $('scan > #resp').html(result);
          console.log('Sucess', result);
        }
      })
      // $('#resp').html(selectedDate)
      widget.hide();
    });

    $('#botao').on('click', function () {

      let input = $('#p2').text().trim()
      if (input == 'p2') {
        $('#p1').text('clicou 1')
        $('#p2').text('Not p2')
        widget.show()
        // $('p').toggle()
        // $('#dtpick').datepicker('show')

        // $('p').html(input)
      } else {
        $('#p1').text('clicou 2')
        $('#p2').text('p2')
        widget.hide()
        // $('#dtpick').datepicker('hide')
        // input = $('p').text('Aqui')
        // $('p').text('Aqui')
      }

      // var selectedDate = $(this).datepicker('getFormattedDate');
      // $('p').html('OK')
    });
  });

*/

  /*  $(document).ready(function () {
    
          $("#spanButton").hide();
    
          var btMoedas = []
    
          // function addCheckbox(name) {
    
          //   const container = $("#cblist");
          //   const inputs = container.find("input");
          //   const id = inputs.length + 1;
    
          //   $("<input />", { type: "checkbox", id: "cb" + id, value: name }).appendTo(container);
          //   $("<label />", { "for": "cb" + id, text: name }).appendTo(container);
          // }
    
          const widget = $("#dtpick").datepicker({
            language: "pt-BR",
            todayHighlight: true,
            container: "div.dtpic",
            format: "dd/mm/yyyy"
          }).hide();
    
    
          widget.on("changeDate", function () {
            widget.hide();
    
            function monta_escolhas() {
              result = {}
    
              let tmp = $(".checkbox");
    
              console.log("Temp = ", tmp);
              const range = [0, 1, 2, 3]
              // moedas_escolhidas = {}
              console.log("btMoedas = ", btMoedas);
              for (i in range) {
                if (btMoedas[i]) {
                  // moedas_escolhidas[`${tmp[i].id}`] = `${tmp[i].name}`
                  result[`${tmp[i].id}`] = `${tmp[i].name}`
                }
              }
              console.log("Monta Escolhas = ", result);
              return result
            }
    
            const selectedDate = widget.datepicker("getFormattedDate");
            const moedas_escolhidas = monta_escolhas()
            const dd = JSON.stringify({ "data": selectedDate, "moedas": moedas_escolhidas })
            console.log("DADO ", dd);
    
    
            // function pegaval(param) {
    
            // const tmp = param["data"];
            // const tmp2 = param["moedas"]
            // const val1 = tmp["bid"].slice(0, -2);
            // const dt = tmp["create_date"].slice(0, -8);
    
            // return `Valor = ${val1} Data = ${dt} moedas=${tmp2}`;
            // }
    
            // $.ajax({
            // url: '/b',
            // type: 'POST',
            // data: dd,
            // dataType: 'json',
            // contentType: 'application/json; charset=utf-8',
            // success: (result, status, request) => {
            // $('.sec1, .sec2').hide();
            // tmpdiv = { 'pp': '<div class="tab" id="tab1"></div>' };
            // $('main').html(tmpdiv.pp);
            // // console.log('Result = ', result);
            // $('#tab1').html(result.response);
            // console.log('Sucess', result.response);
            // }
            // })
    
          });
    
          $('#botao2').on('click', function () {
    
            btMoedas = [
              $('#Dolar').is(':checked'),
              $('#Euro').is(':checked'),
              $('#Libra').is(':checked'),
              $('#Shekel').is(':checked')
            ]
    
            // $('#spanMoedas').text(`Dolar = ${brDolar}`)
            // alert(`btDolar = ${btDolar}\nbtEuro = ${btEuro}\nbtLibra = ${btLibra}\nbtShekel = ${btShekel}`)
    
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
        });*/
 $(document).ready(function () {

    $('#spanButton').hide();
    // $('#botao').hide();
    var btMoedas = []

    // function addCheckbox(name) {

    //   const container = $("#cblist");
    //   const inputs = container.find("input");
    //   const id = inputs.length + 1;

    //   $("<input />", { type: "checkbox", id: "cb" + id, value: name }).appendTo(container);
    //   $("<label />", { "for": "cb" + id, text: name }).appendTo(container);
    // }

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
        // moedas_escolhidas = {}
        console.log('btMoedas = ', btMoedas);
        for (i in range) {
          if (btMoedas[i]) {
            // moedas_escolhidas[`${tmp[i].id}`] = `${tmp[i].name}`
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


      // function pegaval(param) {

      // const tmp = param['data'];
      // const tmp2 = param['moedas']
      // const val1 = tmp['bid'].slice(0, -2);
      // const dt = tmp['create_date'].slice(0, -8);

      // return `Valor = ${val1} Data = ${dt} moedas=${tmp2}`;
      // }

      $.ajax({
        url: '/b',
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

      // $('#spanMoedas').text(`Dolar = ${brDolar}`)
      // alert(`btDolar = ${btDolar}\nbtEuro = ${btEuro}\nbtLibra = ${btLibra}\nbtShekel = ${btShekel}`)

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