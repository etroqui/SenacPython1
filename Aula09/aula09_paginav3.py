from bs4 import BeautifulSoup
import requests
from time import sleep
from os import system
import json
import openpyxl

system('cls')

# Specify the request headers
v_request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

v_arquivo_saida = 'ProdutosPagueMenos2.xlsx'

def getDadosSoup(p_url):
    d_resposta = requests.get(p_url,headers=v_request_headers)
    if d_resposta.status_code == 200:
        d_soup              = BeautifulSoup(d_resposta.text,"html.parser")
        d_pagina            = d_soup.find_all('div',class_='text-center pt-3')
        d_pagina_total      = d_pagina[1].text.strip()[12:13]
        #v_quantidade_produtos   = v_pagina[0].text.strip()
    return d_soup, d_pagina_total

def ConsultaSitePagueMenos(p_url):
    resposta = requests.get(p_url,headers=v_request_headers)
    d_prod_paguemenos = []

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text,"html.parser")
        v_produtos = soup.find_all('div',class_='li')

        for produto in v_produtos:
            v_nome_produto = produto.find('h2').text.strip()
            if not produto.find('strong'):
                v_preco_produto = 'Sem Estoque'
            else:
                v_preco_produto = produto.find('strong').text.strip()

            v_preco_produto = v_preco_produto.replace('R$ ','')
            d_prod_paguemenos.append([
                v_nome_produto,
                v_preco_produto
            ])
        return d_prod_paguemenos

def GravarArquivoXLSX(dados, nome_arquivo, p_paginacao):
    try:
        if p_paginacao == 1:
            # cria o arquivo excel caso verifique que é a primeira pagina
            excel = openpyxl.Workbook()
        else:
            # abre o excel existente ao identificar pagina 2 em diante
            excel = openpyxl.load_workbook(nome_arquivo)
        planilha = excel.active

        for linha in dados:
            planilha.append(linha) # -> adicionar mais infomações

        excel.save(nome_arquivo) # -> fecho a conexão e dou o nome para o arquivo

        print(f'Dados salvo com sucesso no arquivo {nome_arquivo} na pagina {p_paginacao}')

    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))

def getProximaURL(p_ultima_pagina):

    #tem que usar +1 no argumento 2 do range (stop) pois ele nao é inclusivo, ou seja, para fazer 10 vezes, faça range(1,11)
    for i in range(1,p_ultima_pagina+1):
        d_url = f'https://www.superpaguemenos.com.br/hortifruti/?p={i}'
        v_dados = ConsultaSitePagueMenos(d_url)
        GravarArquivoXLSX(v_dados,v_arquivo_saida,i)        

#Inicia com a pagina 1 da paginacao
v_url_base      = "https://www.superpaguemenos.com.br/hortifruti/?p=1"

#retorna o soup com a informacao principal de quantidade de paginas na paginacao dos dados
v_dados_retorno = getDadosSoup(v_url_base)
#esse dado abaixo eu nao uso para nada, porem vou deixar para mostrar como é um retorno numa tupla
#v_soup          = v_dados_retorno[0]
v_ultima_pagina = int(v_dados_retorno[1])

v_url           = getProximaURL(v_ultima_pagina)
