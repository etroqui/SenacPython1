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

    if resposta.status_code == 200:

        d_prod_paguemenos = []

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
            excel = openpyxl.Workbook() # -> criando o excel
        else:
            excel = openpyxl.load_workbook(nome_arquivo + '.xlsx')
        planilha = excel.active # -> a primeira aba ativa

        for linha in dados:
            planilha.append(linha) # -> adicionar mais infomações

        excel.save(nome_arquivo + '.xlsx') # -> fecho a conexão e dou o nome para o arquivo

        print(f'Dados salvo com sucesso no arquivo {nome_arquivo} na pagina {p_paginacao}')

    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))

def getProximaURL(p_soup, p_ultima_pagina):

    for i in range(1,p_ultima_pagina+1):
        d_url = f'https://www.superpaguemenos.com.br/hortifruti/?p={i}'
        v_dados = ConsultaSitePagueMenos(d_url)
        GravarArquivoXLSX(v_dados,'ProdutosPagueMenos',i)        

v_url_base      = "https://www.superpaguemenos.com.br/hortifruti/?p=1"
v_dados_retorno = getDadosSoup(v_url_base)

v_soup          = v_dados_retorno[0]
v_ultima_pagina = int(v_dados_retorno[1])
v_url           = getProximaURL(v_soup,v_ultima_pagina)
