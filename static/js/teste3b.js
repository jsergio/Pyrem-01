   $(document).ready(function () {

      // Inicializa o datepicker dentro do modal
      $('.datepicker-modal').datepicker({
        language: 'pt-BR',
        todayHighlight: true,
        // startDate: '-3d',
        autoclose: true,
        format: "dd/mm/yyyy"
      });

      // Atualiza o valor do campo de entrada quando uma data é selecionada no calendário dentro do modal
      $('.datepicker-modal').on('changeDate', function () {
        var selectedDate = $(this).datepicker('getFormattedDate');
        $('#input').val(selectedDate);
        $('#calendarModal').modal('hide');
      });

      // Evita que o campo de entrada abra o calendário diretamente ao ser clicado
      // $('.datepicker').on('click', function(event) {
      // event.stopPropagation();
      // });
    });
