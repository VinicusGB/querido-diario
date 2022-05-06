from os import chdir, getcwd
from datetime import date, datetime

dt_now = str(date.today().strftime("%Y-%m=%d"))


import fitz as fz

import tabula

BASE_DIR = os.getcwd()
#data_collection\data\3550308\2022-05-06\0c2c4815d12bcbea7d2049c233a9fe7a57f4ac1e.pdf
#"data/3550308/"+ dt_now +"/0c2c4815d12bcbea7d2049c233a9fe7a57f4ac1e.pdf"

with fz.open("data/3550308/2022-05-06/0c2c4815d12bcbea7d2049c233a9fe7a57f4ac1e.pdf") as pdf:
    conteudo = ""
    for pagina in pdf:
        conteudo += pagina.get_text()




'''
#Localizando o início da tabela de dados
indice_dados = conteudo.find('CONCURSO:')

cabecalho_dom = conteudo[:indice_dados-1].replace('\n',' ')
dados = conteudo[indice_dados:]

dados = dados.replace('\n',' ')
dados = dados.replace(' - ',' ')
dados = dados.replace('- ','-')
dados = dados.replace(' -','-')
dados = dados.replace('  ',' ')
dados = dados.replace('   ',' ')

col = 1
position = 0
separadados = dados
linhas = "REG.FUN;ID_CARGO_ANTIGO;ID_CARGO_NOVO;NOME;ID_DE;DE;ID_PARA;PARA;CONCURSO;CARGO\n"

while separadados.find('-') != -1:
    if col == 1:
        position = separadados.find('-')
        if position != -1 and separadados[position-1].isnumeric() and separadados[position+1].isnumeric():
                info = separadados[position-7:position+5]
                info = info.strip()
                #info = info.replace('\n',' ')
                info = info.replace('-', ';')
                linhas = linhas + info + ';'
                #print(f'{separadados[position-7:position]} - {separadados[position-1].isnumeric()} - { separadados[position+1].isnumeric()}')
                #linha.append(info)
                print(f'coluna 01: {info}')
                #separadados = separadados[position+6:]
                if separadados[:position].find('CARGO=') != -1:
                        position_cargo = separadados[:position].find('CARGO=')
                        cargo = separadados[position_cargo+6:position-6]
                        if separadados[:position].find('CONCURSO:') != -1:
                                position_concurso = separadados[:position].find('CONCURSO:')
                                concurso = separadados[position_concurso+9:position_cargo]
                                separadados = separadados[position+6:]
                                cargo = (';' + cargo + ';' + concurso)
                        else:
                                separadados = separadados[position+6:]
                                cargo = (';' + cargo + ';' + concurso)
                else:
                        separadados = separadados[position+6:]
                #print(separadados)
                #break
                col +=1
        else:
            separadados = separadados.replace('-', ' ',1)
            continue
    elif col  == 2:
        position = separadados.find('-')
        if position != -1 and separadados[position-1].isnumeric():
                info = separadados[0:position-6]
                info = info.strip()
                #info = info.replace('\n', ' ')
                linhas = linhas + info + ';'
                #linha.append(info)
                print(f'coluna 02: {info}')
                separadados = separadados[position-6:]
                #print(separadados)
                #break
                col +=1
        else:
            separadados = separadados.replace('-', ' ',1)
            continue
    elif col  == 3:
        position = separadados.find('-')
        if position != -1 and separadados[position-1].isnumeric():
                separadados = separadados.replace('-','*',1)
                position_next = separadados.find('-')
                if position_next != -1 and separadados[position_next-1].isnumeric():
                        position_next = position_next
                else: 
                        separadados = separadados.replace('-', ' ',1)
                        position_next = separadados.find('-')
                info = separadados[0:position_next-6]
                info = info.strip()
                info = info.replace('*',';')
                #info = info.replace('\n',' ')
                linhas = linhas + info + ';'
                #linha.append(info)
                print(f'coluna 03: {info}')
                separadados = separadados[position_next-6:]
                #print(separadados)
                #break
                col +=1
        else:
            separadados = separadados.replace('-', ' ',1)
            continue
    elif col  == 4:
        position = separadados.find('-')
        if position != -1 and separadados[position-1].isnumeric():
                separadados = separadados.replace('-','*',1)
                position_next = separadados.find('-')
                if position_next != -1 and separadados[position_next-1].isnumeric():
                        position_next = position_next
                else: 
                        separadados = separadados.replace('-', ' ',1)
                        position_next = separadados.find('-')
                info = separadados[0:position_next-7]
                info = info.strip()
                info = info.replace('*',';')
                #info = info.replace('\n',' ')
                linhas = linhas + info + cargo + '\n'
                #linha.append(info)
                print(f'coluna 04: {info}')
                separadados = separadados[position+1:]
                #print(separadados)
                #break
                col = 1
        else:
            separadados = separadados.replace('-', ' ',1)
            continue


## Salvando o arquivo final

with open("remocao_2021.csv","w",encoding='utf-8') as arquivo:
    arquivo.write(linhas)
'''

