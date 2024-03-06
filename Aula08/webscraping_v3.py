from bs4 import BeautifulSoup
import requests
from time import sleep
from os import system

system('cls')

# Specify the request headers
v_request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

v_url_1 = "https://www.fundamentus.com.br/detalhes.php?papel=CXSE3"
v_url_2 = "https://www.ibge.gov.br/indicadores.html"

def return_value_1(p_url):
    v_request   = requests.get(p_url,headers=v_request_headers)
    d_soup      = BeautifulSoup(v_request.text, "html.parser")
    d_return    = d_soup.find("td",{"class":"data destaque w3"}).text
    return      d_return

def return_value_2(p_url):
    v_request   = requests.get(p_url,headers=v_request_headers)
    d_soup      = BeautifulSoup(v_request.text, "html.parser")
    d_return    = d_soup.find("p",{"class":"indicador-value"}).text
    return      d_return


v_return_1 = return_value_1(v_url_1)
print(f"\n O valor da Caixa Seguridade no momento é : {v_return_1} ", end="")

v_return_2 = return_value_2(v_url_2)
print(f"\n O valor da inflação IPCA no momento é : {v_return_2} ", end="")

while True:

    v_new_return_1 = return_value_1(v_url_1)
    v_new_return_2 = return_value_2(v_url_2)

    if v_new_return_1 != v_return_1:
        v_return_1 = v_new_return_1
        print(f"\r O valor da Caixa Seguridade no momento é : {v_return_1} ", end="")

    if v_new_return_2 != v_return_2:
        v_return_2 = v_new_return_2
        print(f"\n O valor da inflação IPCA no momento é : {v_return_2} ", end="")

    sleep(10)
