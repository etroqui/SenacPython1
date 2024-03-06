'''
pip install requests --quiet
pip install pandas
pip install beautifulsoup4
'''

'''
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
#import matplotlib.pyplot as plt

print(v_request)
'''

from bs4 import BeautifulSoup
import requests
from time import sleep
from os import system

system('cls')

v_url = "https://www.fundamentus.com.br/detalhes.php?papel=CXSE3"

def stock_price(p_url):
    # Specify the request headers
    d_request_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    v_request   = requests.get(p_url,headers=d_request_headers)
    d_soup      = BeautifulSoup(v_request.text, "html.parser")
    d_price     = d_soup.find("td",{"class":"data destaque w3"}).text
    return      d_price

v_price = stock_price(v_url)
print(f"\n O valor da Caixa Seguridade no momento é : {v_price} ", end="")

while True:
    v_new_price = stock_price(v_url)
    if v_new_price != v_price:
        #v_price = stock_price(v_url)
        v_price = v_new_price
        print(f"\r O valor da Caixa Seguridade no momento é : {v_price} ", end="")
    sleep(1)
