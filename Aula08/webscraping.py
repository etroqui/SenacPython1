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

# Specify the request headers
request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  }

v_url = "https://www.fundamentus.com.br/proventos.php?papel=CXSE3&tipo=2"

v_request   = requests.get(v_url,headers=request_headers)

'''
if v_request.status_code == 200:
    print(f'Request headers: {v_request.request.headers}')
else:
    print(v_request)
'''
    
v_soup      = BeautifulSoup(v_request.text, "html.parser")

#print(v_soup)

v_provents  = v_soup.find_all(string="0,5000")
v_parent    = v_provents[0].parent
print (v_parent)


#v_soup = BeautifulSoup(v_request.text,'html')

#print(v_soup)

#from datetime import date
#print(date.today())
#print(date.isoformat(date.today()))
