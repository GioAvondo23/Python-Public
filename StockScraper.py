#import xlwings as xw
import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np
import time
import matplotlib.pyplot as plt



headers = {'User-Agent': """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"""}




    
url1 ='https://www.investing.com/equities/'

companies = ['apple-computer-inc','nvidia-corp', 'microsoft-corp','google-inc','mastercard-cl-a']
blocks = ['B1', 'B2', 'B3', 'B4', 'B5']
bolocks = ['A1', 'A2', 'A3', 'A4', 'A5']
url = 'https://www.investing.com/equities/nvidia-corp'
url = 'https://www.wikipedia.org'
page = requests.get(url,headers = headers)
soup = BeautifulSoup(page.content, "html.parser")
print(page)
results = soup.find_all('div',class_ = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]')
r = list(str(results))
n = [i for i, x in enumerate(r) if x == '>' ]
n2 = [i for i, x in enumerate(r) if x == '<' ]

a = r[n[0]+1:n2[1]]
a = float(''.join(a))
    
def price(company, url1 = url1):
    url = url1 + company
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all('div',class_ = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]')
    r = list(str(results))
    n = [i for i, x in enumerate(r) if x == '>' ]
    n2 = [i for i, x in enumerate(r) if x == '<' ]

    a = r[n[0]+1:n2[1]]
    a = float(''.join(a))
    return a



"""
wb = xw.Book('WebScraper.xlsx')
sheet = wb.sheets['Sheet1']
count = 0
for company in companies:
    p = price(company)
    sheet[blocks[count]].value = p
    sheet[bolocks[count]].value = company
    count += 1

https://explore.whatismybrowser.com/useragents/parse/693981479-safari-mac-os-x-webkit
    """

