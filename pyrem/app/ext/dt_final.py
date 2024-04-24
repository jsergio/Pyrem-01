def list_to_table(param):
    tmp_dt = param[0][2] # Isso é a data do momento
    tab = '<table class="table caption-top table-bordered tab1 " id="mtab">'
    tab = tab + f"<center> <caption style='color: yellow; background-color: dimgrey'> Cotacão de Moedas em {tmp_dt} </caption>  <thead>";
    tab = tab + '''<tr>
       <th scope="col">#</th>
       <th scope="col">nome</th>
       <th scope="col">valor</th>
       <th scope="col">hora</th>
     </tr>
   </thead>    
   <tbody>'''
    
    i = 0
    for ln in param:
      i = i + 1;
      tab = tab + '<tr> <td>'+str(i)+'</td>'
      for ind,cl in enumerate(ln):
        if ind != 2:
          tab = tab + '<td>' + cl + '</td>';
      tab = tab+'<tr>';
    tab = tab + '</tbody>'
    tab = tab + '</table>'
    print('TABELA = ',tab)
    return tab


def tratar(**arg):
  # print('AQUI ')
  res = []
  if 'p' in arg:
    tmp = arg['p'];
    # print('TYPE tmp ',type(tmp))
    traducao = {'USD':'Dolar','EUR':'Euro','GBP':'Libra','ILS':'Shekel'}
    # print('TMP ',tmp)
    
    for item in tmp:
        # print('item ',item)
        temp_obj = tmp[item]
        # print('TEMP_OBJ ',temp_obj)
        code = temp_obj['code']
        nome = traducao[code]
        bid = temp_obj['bid'];
        tmp_dt = temp_obj['create_date'];
        dt = tmp_dt[0:10];
        dh = tmp_dt[11:];
        res_obj = [nome,bid,dt,dh]
        res.append(res_obj)
        # print('ATTRIB ',nome,bid,dt,dh)
    
  # print('RES_OBJ ',res_obj)
      
  print('RES_PARAM = ', res)
  res2 = list_to_table(res)
  # print('TABLE = ', res2)
  return res2
  