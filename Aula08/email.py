from bs4 import BeautifulSoup
import requests
from time import sleep
from os import system

system('cls')

# Specify the request headers
v_request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def ConsultaSitePagueMenos(p_url):
    resposta = requests.get(p_url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text,"html.parser")
        page = soup.find('div',class_='list-products page-content')
        #print(page)

        prod_paguemenos = []
        for row in page.find_all('div',class_='desc position-relative'):
            produto = row.find('h2').text.strip()
            preco = row.find('strong').text.strip()
            preco = preco.replace('R$ ','')

            prod_paguemenos.append([
                produto,
                preco
            ])
        return prod_paguemenos

def ConsultaSiteSaoVicente(p_url):
    resposta = requests.get(p_url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text,"html.parser")
        page = soup.find('div',class_='searchResults__productGrid js-searchResults__productGrid')
        #print(page)

        prod_saovicente = []

        for row in page.find_all('span',class_='productCard__title'):
            print('oi')
            produto = row.find('span').text.strip()
            preco = '1'
            preco = preco.replace('R$ ','')

            prod_saovicente.append([
                produto,
                preco
            ])
        return prod_saovicente

v_url_1 = "https://www.superpaguemenos.com.br/hortifruti/"
v_url_2 = "https://www.svicente.com.br/Hortifruti-3"

#ConsultaSitePagueMenos(v_url_1)
ConsultaSiteSaoVicente(v_url_2)
