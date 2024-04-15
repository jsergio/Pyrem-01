def obj_to_table(p):
    # tabela = ''
    i = 0
    param = p[0]
    moeda = p[1]
    ndias = p[2]
    nnum1 = len(param)
    def cabeca():
        tabela = '<table class="table caption-top table-bordered tab1 " id="mtab">'
        tabela = tabela + f"<center> <caption id='tit_tab'>Cotacão de {moeda} nos Últimos {nnum1} Dias \
          </caption>  <thead>";
        tabela = tabela + '''<tr>
        <th scope="col">#</th>
        <th scope="col">Data</th>
        <th scope="col">Valor</th>
        <th scope="col">Hora</th>
        </tr>
        </thead>    
        <tbody>'''
        return tabela
    
    cabecalho = cabeca()

    tab3 = ''
    # print('CABECA => ',cabecalho)
    
    for item in param:
      tab3 = tab3+'<tr>';
      i = i + 1;
      tab3 = tab3 + '<td>' + str(i) + '</td>'
      tab3 = tab3 + '<td>'+param[item]['date']+' - '+ param[item]['sem'] + '</td>'
      # print('Linha -> ',tab3)     
      for el in param[item]:
          if ((el in ['date','sem']) == False) :
            tab3 = tab3 + '<td>' + param[item][el] + '</td>';
      tab3 = tab3+'</tr>';
    tab3 = tab3 + '</tbody>'
    tab3 = tab3 + '</table>'
    # print('tab3 = ',tab3)
    tabela = cabecalho+tab3
    # print('Tabela Final -> ',tabela)
    return tabela
