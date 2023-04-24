#Autor: Gabriel Silva dos Santos
#Componente curricular: Algoritmos I
#Concluido em: 19/09/2022
#Declaro que este código foi elaborado somente por mim de forma individual
#sem conter nenhum trecho de código de colega ou de outros autores, tais como
#provindos de de livros e apostilas, páginas ou documentos eletrônicos da 
#internet. Qualquer trecho de código de outra autoria que não é minha será desta- 
#cada com sua fonte, estando eu, ciente, que estes trechos não serão considerados
#para fins de avaliação

#variaveis

#area cada estado / estado menos reflorestado

area_bahia = 0
area_maranhao = 0
area_ceara = 0
area_rio_grande = 0
area_paraiba = 0 
area_pernambuco = 0 
area_alagoas = 0
area_sergipe = 0 
area_piaui = 0

menos_ba = 99999999999999999999999999999999999999
menos_ma = 99999999999999999999999999999999999999
menos_ce = 99999999999999999999999999999999999999
menos_rn = 99999999999999999999999999999999999999
menos_pb = 99999999999999999999999999999999999999
menos_pe = 99999999999999999999999999999999999999
menos_al = 99999999999999999999999999999999999999
menos_se = 99999999999999999999999999999999999999
menos_pi = 99999999999999999999999999999999999999


#quantida de vezes que o estado foi reflorestado

qt_ba = 0
qt_ma= 0 
qt_ce = 0
qt_rn = 0
qt_pb = 0
qt_pe = 0
qt_al = 0
qt_se = 0
qt_pi = 0

#menor-maior - tipo de arvore + area cada tipo de arvore

arvore_cajueiro = 99999999999999999999999999999999999999
arvore_mangueira = 99999999999999999999999999999999999999
arvore_dende = 99999999999999999999999999999999999999
arvore_coqueiro = 99999999999999999999999999999999999999
arvore_bambu = 99999999999999999999999999999999999999
arvore_ipe = 99999999999999999999999999999999999999

cont_cajueiro = 0
cont_mangueira = 0
cont_dende = 0 
cont_coqueiro = 0
cont_bambu = 0
cont_ipe = 0 

maior_arvore = 0
cont = 0

area_cajueiro = 0
area_mangueira = 0 
area_dende = 0
area_coqueiro = 0
area_bambu = 0 
area_ipe = 0

#informações área mais reflorestada

maior = 0

codigo_maior = 0 
cidade_maior = 0 
estado_maior = 0 
area_maior = 0
tipo_arvore_maior = 0



enc = 0
while enc != 'n': 
 
    #entrada de dados

    print ('\nATENÇÃO: recomenda-se que o código da área tenha de 4 - 6 caracteres, para uma melhor visualização da(s) informação(ões) no relatório final.')
    print ('O código da área pode conter numeros e(ou) letras.\n')
    
    codigo = input ('Insira o código da area: ')
    cidade = input ('Insira o nome da cidade: ')

    print ('\nPor favor, digite o estado de acordo com o MENU abaixo:\n'
            'Para cada estado, digite a SIGLA correspondente\n',
            '\nBahia - ba',
            '\nMaranhao - ma',
            '\nCeara - ce',
            '\nRio grande do norte - rn',
            '\nParaiba - pb',
            '\nPernambuco - pe',
            '\nAlagoas - al ',
            '\nSergipe - se',
            '\nPiauí - pi',
            '\n')

        
    estado = input('Digite o nome do estado: ').upper().lower()
    
    while estado != 'ma' and estado !='ba' and estado !='ce' and estado !='rn' and estado != 'pb' and estado !='pe' and estado !='al' and estado !='se' and estado != 'pi':
            print ('\nVALOR INVÁLIDO, DIGITE NOVAMENTE',
            '\n')
            
            print ('Por favor, digite o estado de acordo com o MENU abaixo:\n'
            'Para cada estado, digite a SIGLA correspondente\n',
            '\nBahia - ba',
            '\nMaranhao - ma',
            '\nCeara - ce',
            '\nRio grande do norte - rn',
            '\nParaiba - pb',
            '\nPernambuco - pe',
            '\nAlagoas - al ',
            '\nSergipe - se',
            '\nPiauí - pi',
            '\n')

            estado = input('Digite o nome do estado: ').upper().lower()
    
    print ('\nDigite as dimensões da área (largura e comprimento, em metros)\n')
    largura = float (input('largura: '))
    comprimento = float (input('comprimento: '))
    
    print('\nPor favor, digite o tipo de arvore de acordo com o MENU abaixo:\n'
    '\nCajueiro' ,
    '\nMangueira',
    '\nDende',
    '\nCoqueiro',
    '\nBambu (referente ao Bambu Gigante) ',
    '\nIpe',)

    arvore = input('\nDigite o tipo de arvore: ').upper().lower()

    while arvore != 'cajueiro' and arvore != 'mangueira' and arvore != 'dende' and arvore != 'coqueiro' and arvore != 'bambu' and arvore != 'ipe':

        print ('\nVALOR INVÁLIDO, DIGITE NOVAMENTE!\n')

        print('\nPor favor, digite o tipo de arvore de acordo com o MENU abaixo:\n'
    '\nCajueiro' ,
    '\nMangueira',
    '\nDende',
    '\nCoqueiro',
    '\nBambu (referente ao Bambu Gigante) ',
    '\nIpe')
   
        arvore = input('\nDigite o tipo de arvore: ').upper().lower()

    #condições para direcionamento e computação de dados

    #área por estado

    cont +=1
    
    if estado  == 'ba':
        area_bahia += largura * comprimento
        qt_ba += 1
        menos_ba = area_bahia

    elif estado == 'ma': 
        area_maranhao += largura * comprimento
        qt_ma += 1
        menos_ma = area_maranhao
        
    elif estado == 'ce': 
        area_ceara += largura * comprimento
        qt_ce += 1
        menos_ce = area_ceara

    elif estado == 'rn': 
        area_rio_grande += largura * comprimento
        qt_rn += 1
        menos_rn = area_rio_grande
        
    elif estado == 'pb': 
        area_paraiba += largura * comprimento     
        qt_pb += 1 
        menos_pb = area_paraiba
        
    elif estado == 'pe': 
        area_pernambuco += largura * comprimento
        qt_pe += 1
        menos_pe = area_pernambuco
        
    elif estado == 'al': 
        area_alagoas += largura * comprimento
        qt_al += 1
        menos_al = area_alagoas
        
    elif estado == 'se': 
        area_sergipe += largura * comprimento  
        qt_se += 1
        menos_se = area_sergipe
        
    elif estado == 'pi': 
        area_piaui += largura * comprimento 
        qt_pi += 1
        menos_pi = area_piaui
    
    #area por cada tipo de arvore + qt

    if arvore == 'cajueiro':
        area_cajueiro += largura * comprimento
        cont_cajueiro += 1
        arvore_cajueiro = cont_cajueiro
        
    elif arvore == 'mangueira':
        area_mangueira += largura * comprimento
        cont_mangueira += 1
        arvore_mangueira = cont_mangueira
    
    elif arvore == 'dende':
        area_dende += largura * comprimento
        cont_dende += 1
        arvore_dende = cont_dende
        
    elif arvore == 'coqueiro':
        area_coqueiro += largura * comprimento
        cont_coqueiro += 1
        arvore_coqueiro = cont_coqueiro
        
    elif arvore == 'bambu': 
        area_bambu += largura * comprimento
        cont_bambu += 1
        arvore_bambu = cont_bambu
        
    elif arvore == 'ipe':
        area_ipe += largura * comprimento
        cont_ipe += 1
        arvore_ipe = cont_ipe

    #area mais reflorestada

    if largura * comprimento > maior: 
        maior = largura * comprimento
        estado_maior = estado
        codigo_maior = codigo
        cidade_maior = cidade
        tipo_arvore_maior = arvore

    enc = input ('\nDeseja adicionar mais alguma área? (o programa será fechado logo após a apresentação do relatório) [s/n]: ')

#prints

print ('='*120)
print ('RELATÓRIO FINAL')
print('Obs.: O relatório consta somente com informações referentes aos dados inseridos.\n')

#area reflorestada por estado

print ('\nÁrea total por estado:\n')

if area_bahia > 0:
    print (f' Bahia: {area_bahia}m^2')
if area_maranhao > 0:
    print (f' Maranhão: {area_maranhao}m^2')
if area_ceara > 0:
    print (f' Ceará: {area_ceara}m^2')
if area_rio_grande > 0:
    print (f' Rio Grande do Norte: {area_rio_grande}m^2')
if area_paraiba > 0:
    print (f' Paraíba: {area_paraiba}m^2')
if area_pernambuco > 0:
    print (f' Pernambuco: {area_pernambuco}m^2')
if area_alagoas > 0:
    print (f' Alagoas: {area_alagoas}m^2')
if area_sergipe > 0:
    print (f' Sergipe: {area_sergipe}m^2')
if area_piaui > 0:
    print (f' Piauí: {area_piaui}m^2')

#area total reflorestada

print ('\nÁrea total reflorestada:\n')
print (f' {area_bahia + area_maranhao + area_ceara + area_rio_grande + area_paraiba + area_pernambuco + area_alagoas + area_sergipe + area_piaui}m^2')

#area total reflorestada por cada tipo de arvore:

print ('\nÁrea total reflorestada por cada tipo de árvore:\n')

if area_cajueiro > 0:
    print (f' Cajueiro: {area_cajueiro}m^2')
if area_mangueira > 0:
    print (f' Mangueira: {area_mangueira}m^2')
if area_coqueiro > 0:
    print (f' Coqueiro: {area_coqueiro}m^2')
if area_bambu > 0:
    print (f' Bambu Gigante: {area_bambu}m^2')
if area_ipe > 0:
    print (f' Ipê: {area_ipe}m^2')
if area_dende > 0:
    print (f' Dendê: {area_dende}m^2\n')


#arvore mais/menos usada
print ('\nSe a árvore mais utilizada for igual a menos utilizada, significa que somente ela foi utilizada')

if arvore_cajueiro < arvore_bambu and arvore_cajueiro < arvore_mangueira and arvore_cajueiro < arvore_coqueiro and arvore_cajueiro < arvore_ipe and arvore_cajueiro < arvore_dende:
    print ('\nArvore menos utilizada: Cajueiro')
elif arvore_bambu < arvore_cajueiro and arvore_bambu < arvore_mangueira and arvore_bambu < arvore_coqueiro and arvore_bambu < arvore_ipe and arvore_bambu < arvore_dende:
    print ('\nArvore menos ultilzada: Bambu Gigante')
elif arvore_mangueira < arvore_bambu and arvore_mangueira < arvore_cajueiro and arvore_mangueira < arvore_coqueiro and arvore_mangueira < arvore_dende and arvore_mangueira < arvore_ipe:
    print ('\nArvore menos utilizada: Mangueira')
elif arvore_coqueiro < arvore_mangueira and arvore_coqueiro < arvore_dende and arvore_coqueiro < arvore_cajueiro and arvore_coqueiro < arvore_bambu and arvore_coqueiro < arvore_ipe:
    print ('\nArvore menos utilizada: Coqueiro')
elif arvore_dende < arvore_mangueira and arvore_dende < arvore_bambu and arvore_dende < arvore_cajueiro and arvore_dende < arvore_coqueiro and arvore_dende < arvore_ipe:
    print ('\nArvore menos utilizada: Dende')
elif arvore_ipe < arvore_mangueira and arvore_ipe < arvore_bambu and arvore_ipe < arvore_cajueiro and arvore_ipe < arvore_coqueiro and arvore_ipe < arvore_dende:
    print ('\nArvore menos utilizada: Ipê')
else:
    print('\nNão houve menos/mais utilizada')


if cont_cajueiro > cont_mangueira and cont_cajueiro > cont_dende and cont_cajueiro > cont_coqueiro and cont_cajueiro > cont_bambu and cont_cajueiro > cont_ipe:
    print('Arvore mais utilizada: Cajueiro')
elif cont_mangueira > cont_cajueiro and cont_mangueira > cont_dende and cont_mangueira > cont_coqueiro and cont_mangueira > cont_bambu and cont_mangueira > cont_ipe:
    print('Arvore mais utilizada: Mangueira')
elif cont_dende > cont_mangueira and cont_dende > cont_cajueiro and cont_dende > cont_coqueiro and cont_dende > cont_bambu and cont_dende > cont_ipe:
    print('Arvore mais utilizada: Dendê')
elif cont_coqueiro > cont_mangueira and cont_coqueiro > cont_dende and cont_coqueiro > cont_cajueiro and cont_coqueiro > cont_bambu and cont_coqueiro > cont_ipe:
    print('Arvore mais utilizada: Coqueiro')
elif cont_bambu > cont_mangueira and cont_bambu > cont_dende and cont_bambu > cont_coqueiro and cont_bambu > cont_cajueiro and cont_bambu > cont_ipe:
    print('Arvore mais utilizada: Bambu Gigante')
elif cont_ipe > cont_mangueira and cont_ipe > cont_dende and cont_ipe > cont_coqueiro and cont_ipe > cont_cajueiro and cont_ipe > cont_bambu:
    print('Arvore mais utilizada: Ipê ')


#informações maior area

print('\nInformações da maior área reflorestada:\n')

print (f' Código: {codigo_maior}')
print (f' Estado: {estado_maior}')
print (f' Cidade: {cidade_maior}')
print (f' Área: {maior}m^2')
if tipo_arvore_maior == 'bambu':
    print(' Árvore: Bambu Gigante')
else:
    print (f' Árvore: {tipo_arvore_maior}')

#quantidade de area por estado

print ('\nQuantidade de áreas reflorestadas por estado:\n')

if qt_ba != 0:
    print (f' Bahia: {qt_ba}')
if qt_ma !=0:
    print (f' Maranhão: {qt_ma}')
if qt_ce != 0:
    print (f' Ceará: {qt_ce}')
if qt_rn != 0:
    print (f' Rio Grande do Norte: {qt_rn}')
if qt_pb != 0:
    print (f' Paraíba: {qt_pb}')
if qt_pe != 0:
    print (f' Pernambuco: {qt_pe}')
if qt_al != 0:
    print (f' Alagoas: {qt_al}')
if qt_se != 0:
    print (f' Sergipe: {qt_se}')
if qt_pi != 0:
    print (f' Piauí: {qt_pi}')

#estado menos reflorestado

if menos_ba < menos_ma and menos_ba < menos_ce and menos_ba < menos_rn and menos_ba < menos_pb and menos_ba < menos_pe and menos_ba < menos_al and menos_ba < menos_se and menos_ba < menos_pi:
    print ('\nEstado menos reflorestado: Bahia\n')
elif menos_ma < menos_ba and menos_ma < menos_ce and menos_ma < menos_rn and menos_ma < menos_pb and menos_ma < menos_pe and menos_ma < menos_al and menos_ma < menos_se and menos_ma < menos_pi:
    print ('\nEstado menos reflorestado: Maranhão\n')
elif menos_ce < menos_ba and menos_ce < menos_ma and menos_ce < menos_rn and menos_ce < menos_pb and menos_ce < menos_pe and menos_ce < menos_al and menos_ce < menos_se and menos_ce < menos_pi:
    print ('\nEstado menos reflorestado: Ceará\n')
elif menos_rn < menos_ba and menos_rn < menos_ma and menos_rn < menos_ce and menos_rn < menos_pb and menos_rn < menos_pe and menos_rn < menos_al and menos_rn < menos_se and menos_rn < menos_pi:
    print ('\nEstado menos reflorestado: Rio Grande do Norte\n')
elif menos_pb < menos_ba and menos_pb < menos_ma and menos_pb < menos_ce and menos_pb < menos_rn and menos_pb < menos_pe and menos_pb < menos_al and menos_pb < menos_se and menos_pb < menos_pi:
    print ('\nEstado menos reflorestado: Paraíba\n')
elif menos_pe < menos_ba and menos_pe < menos_ma and menos_pe < menos_ce and menos_pe < menos_rn and menos_pe < menos_pb and menos_pe < menos_al and menos_pe < menos_se and menos_pe < menos_pi:
    print ('\nEstado menos reflorestado: Pernambuco\n')
elif menos_al < menos_ba and menos_al < menos_ma and menos_al < menos_ce and menos_al < menos_rn and menos_al < menos_pb and menos_al < menos_pe and menos_al < menos_se and menos_al < menos_pi:
    print ('\nEstado menos reflorestado: Alagoas\n')
elif menos_se < menos_ba and menos_se < menos_ma and menos_se < menos_ce and menos_se < menos_rn and menos_se < menos_pb and menos_se < menos_pe and menos_se < menos_al and menos_se < menos_pi:
    print ('\nEstado menos reflorestado: Sergipe\n')
elif menos_pi < menos_ba and menos_pi < menos_ma and menos_pi < menos_ce and menos_pi < menos_rn and menos_pi < menos_pb and menos_pi < menos_pe and menos_pi < menos_al and menos_pi < menos_se:
    print ('\nEstado menos reflorestado: Piauí\n')

#e finalmente, fim :D