        $(document).ready(function () {           
          
          console.log('ENTER CLICADO')          
    
          const traducao = {'Dolar':'USD-BRL','Euro':'EUR-BRL','Libra':'GBP-BRL','Shekel':'ILS-BRL'}
         
          let vnum1 = $('#num1').val();
         
          let vmoeda = $('.radio:checked').val()
         
          $('#aaa').html(`${vmoeda} - ${vnum1}`)
          
          // $('#bbb').text(vmoeda)

          $('input:radio').change(function() {
               vmoeda = $('.radio:checked').val()
               $('#bbb').html(`${vmoeda} - ${vnum1}`)
              //  $('#bbb').text(vmoeda)
              //  alert('Alo Gente');
            })

            $('#num1').change(function() {
              vnum1 = $('#num1').val()
              // vmoeda = $('.radio:checked').val()
              $('#aaa').html(`${vmoeda} - ${vnum1}`)
           })
         
          //  nome_moeda = vmoeda
          //  vmoeda = traducao[vmoeda]
        
            
          
            // dd = monta_dados()
            //  console.log('DD2',dd);
            $('#botao').click(function(){
       
              nome_moeda = vmoeda
              vmoeda = traducao[vmoeda]
          
              const url = `https://economia.awesomeapi.com.br/json/daily/${vmoeda}/${vnum1}/`
              console.log('URL -> ',url)
               
               //  url = url + `${url}/${vnum1}/`
              const dd = JSON.stringify({'obj_res':[url,nome_moeda,vnum1]})  
              console.log('DD -> ',dd);
             //  return dd 
             
              $.ajax({
                url: '/dias',
                type: 'POST',
                data: dd,
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                success: (result, status, request) => {
                  // console.log('RESULT ->', result);
                  // $('.sec1, .sec2').hide();
                  $('#cabeca1').hide()
                  const tmpdiv = '<div class="tab" id="tab2"></div>';
                  $('main').html(tmpdiv);
                  // res = tabelisa(result.response)
                  // res = JSON.stringify(result)
                  // res2 = JSON.stringify(request)
              
                  console.log('Tabela = ',result);
                  $('.tab').html(result);
                  // console.log('Sucess', result);
                }
              
            })
          })
        })
