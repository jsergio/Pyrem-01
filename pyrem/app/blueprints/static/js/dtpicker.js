 $(document).ready(function () {
    $.fn.datepicker.defaults = {
      hide: true,
      autoclose: true,
      beforeShowDay: $.noop,
      calendarWeeks: true,
      clearBtn: true,
      // daysOfWeekDisabled: [],
      // endDate: Infinity,
      // forceParse: true,
      // format: 'dd/mm/yyyy',
      // keyboardNavigation: true,
      language: 'pt-BR',
      minViewMode: 0,
      multidate: false,
      multidateSeparator: '-',
      orientation: "auto",
      rtl: false,
      // startDate: -Infinity,
      startView: 0,
      // todayBtn: false,
      todayHighlight: true,
      weekStart: 0,
      onSelect: function (dateText, inst) {
        var date = $(this).val();
        alert(date);
      }
    };


    let widget = $("#mdtpic").datepicker({ hide: true });


    $('#toggleDatepicker').on('onClick', function () {
      $(p).html('OK')
      let btnnow = $('#toggleDatepicker').text()
      // var btnnow = $(this).datepicker("option", "buttonText");
      $(p).html(btnnow)
      if (btnnow == 'Abrir') {
        $(widget).show()
        $(this).text('Fechar')
      }
      else {
        $('#mdtpic').datepicker().hide()
        $(this).text('Abrir')
      }
    })
    // Inicializa o datepicker dentro do modal
    // $('.datepicker-modal').datepicker({
    //   // hide,
    //   language: 'pt-BR',
    //   todayHighlight: true,
    //   // startDate: '-3d',
    //   container: '.sec2',
    //   autoclose: true,
    //   format: "dd/mm/yyyy"
    // });

    // Atualiza o valor do campo de entrada quando uma data é selecionada no calendário dentro do modal
    // $('#mdtpic').datepicker.on('onSelect', function () {
    //   $(p).html('Entrei')
    //   var selectedDate = $('#mdtpic').datepicker('getFormateDate')//$(this).datepicker('getFormattedDate');
    //   $('p').html(selectedDate)
    //   // $('p').text(selectedDate);
    //   // $('#mdtpic').hide();
    // });

    // Evita que o campo de entrada abra o calendário diretamente ao ser clicado
    // $('.datepicker').on('click', function(event) {
    //     event.stopPropagation();
    // });
  });
